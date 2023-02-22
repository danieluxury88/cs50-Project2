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
    starting_big = models.FloatField()
    image_url = models.URLField(max_length=100)

    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    status = models.BooleanField(default=True)


class Bid(models.Model):
    amount = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class WatchList(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
