from django.db.models.query import QuerySet
import rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import PostHashtagSerializer, PostSerializer
from .models import Post, Hashtag

class CreatePost(APIView):
   permission_classes = [IsAuthenticated]
   serializer_class = PostHashtagSerializer

   def post(self, request, form=None):
        serializer = self.serializer_class(data=request.data)
       
        if serializer.is_valid():
           author = request.user
           title = serializer.data.get('title')
           body = serializer.data.get('body')
           hashtags = serializer.data.get('hashtag').split(' ')
           post = Post.objects.create(author=author, body=body)
           for hashtag in hashtags:
              selected_hashtag, created = Hashtag.objects.get_or_create(name=hashtag)
              selected_hashtag.post.add(post)
           return Response({'Message': 'Your post created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ViewHashtagPost(ListAPIView):
   permission_classes = [IsAuthenticated]
   serializer_class = PostSerializer

   def get_queryset(self):
      hashtag = self.kwargs['hashtag']
      # hashtag_list = []
      # hashtag_ins = Hashtag.objects.filter(name=hashtag)
      # hashtag_list = [i.post for i in hashtag_ins]
      queryset = Post.objects.filter(hashtag__name=hashtag)

      print(queryset)
      return queryset
