from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import ProfileSerializer, RelationSerializer
from .models import Profile, Relation
from account.models import Account

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


class FollowUser(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RelationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            from_user = request.user
            to_user_id = serializer.data.get('to_user')
            to_user = Account.object.get(id=to_user_id)
            is_relation = Relation.objects.filter(from_user=from_user, to_user=to_user).exists()
            if not is_relation:
                Relation.objects.create(from_user=from_user, to_user=to_user)
                return Response({'Message': f'You follow {to_user}'}, status=status.HTTP_201_CREATED)
            
            return Response({'Message': 'You have already followed this user'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    