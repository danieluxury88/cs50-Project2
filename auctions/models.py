from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category_type = models.CharField(max_length=20)

    def __str__(self):
        return self.category_type


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
        return f"{self.title} Publisher: {self.publisher}"


class Bid(models.Model):
    amount = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.author} said: {self.comment}"


class WatchList(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
