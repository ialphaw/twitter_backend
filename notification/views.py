from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import NotifSerializer
from .models import Notif

class Notification(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotifSerializer
    

    def get_queryset(self):
        user = self.request.user
        queryset = Notif.objects.filter(following=user)
        for query in queryset:
            if query.is_read2:
                query.is_read = True
            query.is_read2 = True
            query.save()
        return queryset




