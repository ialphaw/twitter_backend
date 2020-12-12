from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from post.models import Post
from user_profile.models import Relation
from post.serializers import PostSerializer

class HomeView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        related_list = []
        relations = Relation.objects.filter(from_user=user)
        related_list = [rec.to_user for rec in relations]
        queryset = Post.objects.filter(author__in=related_list)
        print(relations)
        return queryset
