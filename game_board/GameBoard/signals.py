from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import *


@receiver(post_save, sender=Post)
def my_handler(sender, instance, created, **kwargs):
    if not created:
        return
    user_post = instance.author
    send_mail(
        'Ваше обьявление создано',
        f'Здравствуйте {user_post.username} создан отклик на ваше объявление.',
        'host@mail.ru',
        [author_post.email],
        fail_silently=False
    )


@receiver(post_save, sender=Comment)
def my_handler(sender, instance, created, **kwargs):
    if not created and instance.status is True:
        user_comment = instance.author
        send_mail(
        'Ваше отклик принят',
        f'Здравствуйте {user_comment.username} ваш отклик был принят.',
        'host@mail.ru',
        [user_comment.email],
        fail_silently=False
        )

@receiver(post_save, sender=Post)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs[ 'action' ] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)
