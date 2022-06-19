from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post


class testCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.get_or_create(email='test@gmail.com', is_active=True, username='test_user')
        user.set_password('test@123')
        user.save()
        test_post = Post.objects.create(title='Post Title', content='Post Content', user=user)

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        user = f'{post.user}'
        title = f'{post.title}'
        content = f'{post.content}'
        self.assertEqual(user, 'test@gmail.com')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
