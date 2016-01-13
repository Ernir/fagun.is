from django.contrib import admin
from django.db import models
from django import forms
from adminsortable2.admin import SortableAdminMixin
from fagun.models import Article, SidebarEntry


class SidebarAdmin(SortableAdminMixin, admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'class': 'ckeditor'})
        },
    }

    class Media:
        css = {"all": ("admin_style.css",)}
        js = ('//cdn.ckeditor.com/4.4.7/standard/ckeditor.js',)


admin.site.register(Article)
admin.site.register(SidebarEntry, SidebarAdmin)