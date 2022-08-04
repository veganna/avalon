from django.db import models
#from model_utils.models import TimeStampedModel
from mainsite.models import nftUsers as User
import os


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, null=False, blank=True)

    def get_user(self):
        return User.objects.get(id=self.user.id)

    def __str__(self):
        return self.text

class Post(models.Model):
    front_description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    meta_description = models.CharField(max_length=500, null=False, blank=True)
    meta_keywords = models.CharField(max_length=500, null=False, blank=True)
    title = models.CharField(max_length=500, null=False)
    content = models.TextField(null=False)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=500, null=False, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    schedule_date = models.DateTimeField(null=False, blank=True)
    approved = models.BooleanField(default=False)

    def get_author(self):
        return User.objects.get(username=self.author)

    def get_comments(self):
        return Comment.objects.filter(post=self)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/post/%s/" % self.slug



