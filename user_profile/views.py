from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import AddItemProperty, SetItemValues, AddPurchase
from recombee_api_client.api_requests import RecommendItemsToItem, SearchItems, Batch, ResetDatabase

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
            queryset = Relation.objects.filter(
                from_user=from_user, to_user=to_user)
            if not queryset.exists():
                Relation.objects.create(from_user=from_user, to_user=to_user)

                client = RecombeeClient(
                    'ialphaw-prod', 'Izv7jJXeqzvznfVvaZA0dQh3j1C4B8ewNKIy4N5Vp5HJShQy94BlMgLEGSS7EMNF')

                req = AddPurchase(from_user.username, to_user.username, cascade_create=True)
                client.send(req)

                try:
                    recommended = client.send(
                        RecommendItemsToItem(
                            f'{from_user.username}', f'{to_user.username}', 3)
                    )
                except:
                    recommended = None

                print(recommended)

                return Response({'Message': f'You follow {to_user}', 'suggestions': recommended}, status=status.HTTP_201_CREATED)

            return Response({'Message': 'You have already followed this user'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class UnFollowUser(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RelationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            from_user = request.user
            to_user_id = serializer.data.get('to_user')
            to_user = Account.object.get(id=to_user_id)
            queryset = Relation.objects.filter(
                from_user=from_user, to_user=to_user)
            if queryset.exists():
                relation = queryset.first()
                relation.delete()
                return Response({'Message': f'You un-follow {to_user}'}, status=status.HTTP_201_CREATED)

            return Response({'Message': 'You don\'t follow this user'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
