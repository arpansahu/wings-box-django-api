import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from blog.models import Post
from accounts.models import Account
from celery import shared_task

@shared_task
def process_json_file(file_obj):
    count = 0
    for post_data in file_obj:
        user = Account.objects.filter(id=post_data['userId']).first()
        if user:
            if not Post.objects.filter(id=post_data['id']):
                post = Post(id=post_data['id'], title=post_data['title'], content=post_data['body'], user=user)
                post.save()
                count += 1
    return '{} posts created with success!'.format(count)
