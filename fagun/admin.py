from django.contrib import admin
from django.db import models
from django import forms
from adminsortable2.admin import SortableAdminMixin
from fagun.models import NewsArticle, SidebarEntry, Recipe, SubPage


class CkEditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'class': 'ckeditor'})
        },
    }

    class Media:
        css = {"all": ("admin_style.css",)}
        js = ('//cdn.ckeditor.com/4.4.7/standard/ckeditor.js',)


class SidebarEntryAdmin(SortableAdminMixin, CkEditorAdmin):
    pass


class NewsArticleAdmin(CkEditorAdmin):
    exclude = ("slug", )


class RecipeAdmin(CkEditorAdmin):
    exclude = ("slug", )


class SubPageAdmin(CkEditorAdmin):
    exclude = ("slug", )

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(SidebarEntry, SidebarEntryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(SubPage, SubPageAdmin)