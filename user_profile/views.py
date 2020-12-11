from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer
from .models import Profile


class ShowProfile(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


class ShowUserProfile(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    model = Profile

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = Profile.objects.filter(user__username=username)
        return queryset
