from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User, Category, Auction, Comment, Bid


def index(request):
    active_listings = Auction.objects.filter(status=True)
    return render(request, "auctions/index.html", {
        "active_listings": active_listings,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def publish(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/publish.html", {
            "categories": categories,
        })
    else:
        auction_title = request.POST["title"]
        auction_category = request.POST["category"]
        obj_category = Category.objects.get(category_type=auction_category)
        auction_description = request.POST["description"]
        auction_starting_price = request.POST["start_price"]
        auction_image_url = request.POST["image_url"]
        auction_publisher = request.user

        auction = Auction(title=auction_title, description=auction_description,
                          starting_price=auction_starting_price,
                          current_price=auction_starting_price,
                          image_url=auction_image_url, publisher=auction_publisher,
                          category=obj_category)
        auction.save()
        return index(request)


def details(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    comments = Comment.objects.filter(auction=auction)
    return render(request, 'auctions/details.html', {
        "auction": auction,
        "comments": comments,
    })


def post_comment(request):
    author = request.user
    comment = request.POST["comment"]
    auction_id = request.POST["auction_id"]
    auction = Auction.objects.get(pk=auction_id)
    if not comment:
        messages.warning(request, 'Not empty messages allowed')
    else:
        auction_comment = Comment(comment=comment, author=author, auction=auction)
        auction_comment.save()

    return details(request, auction_id)


def close_auction(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    auction.status = False
    auction.save()
    messages.warning(request, 'Auction closed!')
    return details(request, auction_id)


def post_bid(request, auction_id):
    if request.method == "POST":
        auction = Auction.objects.get(pk=auction_id)
        offered_price = int(request.POST["offered_price"])
        if offered_price <= auction.current_price:
            messages.warning(request, 'Bid should be higher than current price')
        else:
            auction.current_price = offered_price
            auction.save()
            bid = Bid(amount=offered_price, bidder=request.user, item=auction)
            bid.save()
            messages.success(request, 'Bid placed!')

        return details(request, auction_id)




