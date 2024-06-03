from django.urls import path
from .views import *


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('comment/', Comment.as_view(), name='comment'),
   path('<int:pk>/', CommentDetail.as_view()),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('comment/edit/', CommentUpdate.as_view(), name='comment_update'),
   path('comment/delete/', CommentDelete.as_view(), name= 'comment_delete'),

]