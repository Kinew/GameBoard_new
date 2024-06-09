from django.contrib import admin
from .models import *
from django import forms
from GameBoard.models import Post
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscription)
admin.site.register(Comment)