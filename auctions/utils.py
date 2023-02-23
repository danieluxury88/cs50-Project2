from .models import Auction, Bid, Watchlist, Category, Comment


def get_all_listings():
    return Auction.objects.all()


def get_all_closed_listings():
    return Auction.objects.filter(status=False)


def get_all_active_listings():
    return Auction.objects.filter(status=True)


def accept_bid(auction, offered_price, request):
    auction.current_price = offered_price
    auction.save()
    bid = Bid(amount=offered_price, bidder=request.user, item=auction)
    bid.save()


def finalize_auction(auction_id):
    auction = get_auction(auction_id)
    auction.status = False
    auction.save()


def is_item_on_watchlist(user, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    watchlist = Watchlist.objects.filter(item=auction, user=user)
    return watchlist.exists()


def get_item_on_watchlist(user, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    watchlist_item = Watchlist.objects.filter(item=auction, user=user)
    return watchlist_item


def get_auctions_watched_by_user(user):
    return Auction.objects.filter(watchlist__user=user)


def get_all_categories():
    return Category.objects.all()


def get_category(category_name):
    return Category.objects.get(name=category_name)


def get_all_active_listings_in_category(category_name):
    category = get_category(category_name)
    return Auction.objects.filter(category=category)


def get_auction_comments(auction):
    return Comment.objects.filter(auction=auction)


def get_auction(auction_id):
    return Auction.objects.get(pk=auction_id)


def get_all_bids():
    return Bid.objects.all()


def get_all_auction_bids(auction):
    return Bid.objects.filter(item=auction)


def get_highest_auction_bid(auction):
    return get_all_auction_bids(auction).order_by('amount').last()


def get_highest_bid_auction_closed(auction):
    if auction.status == False:
        return get_all_auction_bids(auction).order_by('amount').last()


def get_auction_winner(auction):
    if get_highest_bid_auction_closed(auction) is not None:
        return get_highest_auction_bid(auction).bidder


def is_auction_winner(auction, user):
    if get_auction_winner(auction) is None:
        return False
    return user == get_auction_winner(auction)


def get_all_highest_bids():
    auctions = get_all_listings()
    return auctions


def get_all_auctions_won_by_user(user):
    won_auctions = []
    closed_auctions = get_all_closed_listings()
    for closed_auction in closed_auctions:
        if user == get_auction_winner(closed_auction):
            won_auctions.append(closed_auction)
    return won_auctions
