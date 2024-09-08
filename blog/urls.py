from django.urls import path
from blog.views import home, post_list

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='post_list'),
]
