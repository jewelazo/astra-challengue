from rest_framework import viewsets, status
from .models import Post
from .serializers import PostSerializer
from .pagination import CustomPageNumberPagination
from rest_framework.response import Response


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = CustomPageNumberPagination

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        author_name = request.headers.get('X-Author')

        if post.author != author_name:
            return Response(
                {'detail': 'You do not have permission to delete this post.'},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(request, *args, **kwargs)