from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
        queryset = BlogPost.objects.all()
        serializer_class = BlogPostSerializer

        def delete(self, *args, **kwargs):
                BlogPost.objects.all().delete()
                return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostURD(generics.RetrieveUpdateDestroyAPIView):
        queryset = BlogPost.objects.all()
        serializer_class = BlogPostSerializer
        lookup_field = "pk"



class BlogListPost(APIView):
        def get(self, request, format=None):
                # Get the title, if None (no entry), then default to emtpy string.
                title = request.query_params.get("title", "")

                if title:
                        blog_posts = BlogPost.objects.filter(title__icontains=title)
                else:
                        blog_posts = BlogPost.objects.all()

                serializer = BlogPostSerializer(blog_posts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)