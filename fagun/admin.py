from django.contrib import admin
from django.db import models
from django import forms
from adminsortable2.admin import SortableAdminMixin
from fagun.models import NewsStory, SidebarEntry, EducationalArticle, \
    SubPage, Tag, Author


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
    readonly_fields = ("slug", )


class RecipeAdmin(CkEditorAdmin):
    readonly_fields = ("slug", )


class SubPageAdmin(CkEditorAdmin):
    readonly_fields = ("slug", )


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ("slug", )


admin.site.register(NewsStory, NewsArticleAdmin)
admin.site.register(SidebarEntry, SidebarEntryAdmin)
admin.site.register(EducationalArticle, RecipeAdmin)
admin.site.register(SubPage, SubPageAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author)