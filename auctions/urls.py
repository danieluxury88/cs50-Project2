from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("publish", views.publish, name="publish"),
    path("details/<int:auction_id>", views.details, name="details"),
    path("post_comment>", views.post_comment, name="post_comment"),
    path("close_auction/<int:auction_id>", views.close_auction, name="close_auction"),
    path("post_bid/<int:auction_id>", views.post_bid, name="post_bid"),
    path("toggle_watchlist", views.toggle_watchlist, name="toggle_watchlist"),
    path("view_watchlist", views.view_watchlist, name="view_watchlist"),
    path("won_listings", views.won_listings, name="won_listings"),
]
