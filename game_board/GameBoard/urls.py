from django.urls import path
from .views import PostList, PostCreate


urlpatterns = [
   path('', PostList.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('comment/', Comment.as_view(), name='comment'),
]