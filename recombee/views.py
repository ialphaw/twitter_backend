from rest_framework.decorators import api_view

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import AddItemProperty, SetItemValues, AddPurchase
from recombee_api_client.api_requests import RecommendItemsToItem, SearchItems, Batch, ResetDatabase
from rest_framework.response import Response

from user_profile.models import Profile

client = RecombeeClient(
    'ialphaw-prod', 'Izv7jJXeqzvznfVvaZA0dQh3j1C4B8ewNKIy4N5Vp5HJShQy94BlMgLEGSS7EMNF')

@api_view(['GET'])
def create_user_db(request):
    # client.send(ResetDatabase())
    client.send(AddItemProperty('username_to', 'string'))

    profiles = Profile.objects.all()
    requests = []

    for profile in profiles:
        requests.append(SetItemValues(
            f'{profile.user.username}',
            {
                
            },
            cascade_create=True 
        ))
    
    print(requests)
    client.send(Batch(requests))
    return Response({'msg': 'ok'})
    