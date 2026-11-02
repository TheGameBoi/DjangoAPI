from django.urls import path
from . import views



urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>", views.BlogPostURD.as_view(), name="update"),
    path("blogposts/blogs/", views.BlogListPost.as_view(), name="blog-view-list"),
]
