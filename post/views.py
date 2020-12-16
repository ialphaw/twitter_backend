from django.db.models.query import QuerySet
import rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import PostHashtagSerializer, PostSerializer, RetweetSerializer, LikeSerializer
from .models import Post, Hashtag, Like
from utilities.hashtag import get_hashtag


class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostHashtagSerializer

    def post(self, request, form=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            author = request.user
            title = serializer.data.get('title')
            body = serializer.data.get('body')
            post = Post.objects.create(author=author, body=body)
            hashtags = get_hashtag(body)
            for hashtag in hashtags:
                selected_hashtag, created = Hashtag.objects.get_or_create(
                    name=hashtag)
                selected_hashtag.post.add(post)
            return Response({'Message': 'Your post created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ViewHashtagPost(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        hashtag = self.kwargs['hashtag']
        queryset = Post.objects.filter(hashtag__name=hashtag)
        return queryset


class Search(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        word = self.kwargs['word']
        queryset = Post.objects.filter(body__icontains=word)
        return queryset


class Retweet(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RetweetSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            post_id = serializer.data.get('post_id')
            post = Post.objects.get(id=post_id)
            retweeted_from = post.author
            retweeted_by = request.user

            Post.objects.create(author=request.user, body=post.body, is_retweeted=True,
                                retweeted_from=retweeted_from, retweeted_by=retweeted_by)

            return Response({'Message': 'Retweet successfull'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeAPost(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            post_id = serializer.data.get('post')
            post_result = Post.objects.filter(id=post_id)
            post = post_result.first()
            is_like = Like.objects.filter(user=user, post=post).exists()
            if post_result.exists():
                if not is_like:
                    Like.objects.create(user=user, post=post)
                    return Response({'Message': 'you like this post'}, status=status.HTTP_200_OK)
                
                return Response({'Message': 'you already liked this post'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            return Response({'Message': 'the post does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class UnLikeAPost(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            post_id = serializer.data.get('post')
            post_result = Post.objects.filter(id=post_id)
            post = post_result.first()
            is_like = Like.objects.filter(user=user, post=post)
            if post_result.exists():
                if is_like.exists():
                    is_like.delete()
                    return Response({'Message': 'you un-like this post'}, status=status.HTTP_200_OK)
                
                return Response({'Message': 'you didn\'t like this post at first'})
            
            return Response({'Message': 'the post does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

