from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer


class PostList(APIView):
    def get(self, request, format=None):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdate(APIView):
    def patch(self, request, pk):
        post_object = Post.objects.get(pk=pk)
        serializer = PostSerializer(post_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post_object = Post.objects.filter(pk=pk).first()
        if post_object is not None:
            post_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
