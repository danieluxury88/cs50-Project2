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
]
