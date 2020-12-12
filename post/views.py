from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import PostSerializer
from .models import Post

class CreatePost(APIView):
   permission_classes = [IsAuthenticated]
   serializer_class = PostSerializer

   def post(self, request, form=None):
        serializer = self.serializer_class(data=request.data)
       
        if serializer.is_valid():
           author = request.user
           title = serializer.data.get('title')
           body = serializer.data.get('body')
           Post.objects.create(author=author, title=title, body=body)
           return Response({'Message': 'Your post created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
