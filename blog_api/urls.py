from .views import PostList, FileUploadView
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('upload/', FileUploadView.as_view(), name='upload')
]