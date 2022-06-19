import json

from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from task.tasks import process_json_file

# Display Posts

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]


# views.py
class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        file_obj = request.FILES['image']
        print('Inside File Upload')
        if not file_obj.name.endswith('json'):
            return Response({'message': 'File Format Should be Json'}, status=400)
        process_json_file.delay(json.load(file_obj))
        return Response({'message': f'Successfully processing of {file_obj} started'}, status=200)
