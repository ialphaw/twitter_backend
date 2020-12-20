from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .documents import PostDocument
from post.serializers import PostSerializer
from post.models import Post

import json

class ElasticSearch(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True)
    def result(self, request, pk=None):
        q = pk
        posts = PostDocument.search().query('match', body=q).execute()

        # result_list = []

        # for post in posts:
        #     result_list.append(post.to_dict())

        return Response(posts.to_dict())
