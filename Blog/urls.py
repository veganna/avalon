from django.urls import path
from .views import *

app_name='Blog'

urlpatterns = [
    path('', blogList, name='blogList'),
    path('post/<slug>/', blogDetail, name='blogDetail'),
    path('tag/<tag>/', tagChoose, name='tagChoose'),
    path('search/', blogSearch, name='postSearch'),
    path('author/<username>', blogSearchByAuthor, name='postSearchByAuthor'),
]