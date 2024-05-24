from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    pass


class Category(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spillmaster', 'Мастера заклинаний'),
    )


class Article(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = RichTextUploadingField()
    category = models.CharField(max_length=12, choices=TYPE, default='tank')
    dateCreations = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    pass

class Comment(models.Model):
    commentArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreations = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
