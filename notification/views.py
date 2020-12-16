from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import NotifSerializer
from .models import Notif

class Notification(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotifSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Notif.objects.filter(Q(following=user) | Q(post__author=user))
        return queryset


class ReadNotification(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = self.request
        queryset = Notif.objects.filter(Q(following=user) | Q(post__author=user))
        for query in queryset:
            query.is_read = True
            query.save()
        return Response({'Message': 'Notification is_read is True'})
