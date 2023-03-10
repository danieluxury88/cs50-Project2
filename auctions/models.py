from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Auction(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    starting_price = models.IntegerField()
    current_price = models.IntegerField()
    image_url = models.URLField(max_length=2083)

    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    status = models.BooleanField(default=True)

    def __str__(self):
        state = "active" if self.status else "inactive"
        # output = "{:>30}\tPublisher: {:>10}\t Status:{:>10}".format(self.title, self.publisher.username, state)
        return f"{self.title} Publisher: { self.publisher} State: {state} Current Price: {self.current_price}"


class Bid(models.Model):
    amount = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="winner")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} bidder: {self.bidder} amount: {self.amount}"


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.author} said: {self.comment}"


class Watchlist(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}\t\tItem: {self.item}"


