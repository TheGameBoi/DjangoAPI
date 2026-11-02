from django.urls import path, include
from . import views



urlspatterns = [
    path("blogposts/", views.BlogPostList.as_view(), name="blogpost-view-create")

]
