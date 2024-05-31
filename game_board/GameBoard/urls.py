from django.urls import path
from game_board import views
# Импортируем созданное нами представление
from .views import PostList, PostCreate


urlpatterns = [
   path('', PostList.as_view()),
   path('post/create/', views.PostCreate.as_view(), name='post_create'),
]