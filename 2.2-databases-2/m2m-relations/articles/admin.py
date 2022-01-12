from django.contrib import admin

from .models import Article, Scope, ArticleScope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_values = [form.cleaned_data.get('main_tag', False) for form in self.forms]
        if sum(main_tag_values) > 1:
            raise ValidationError('Должен быть только один основной тег')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    inlines = [ArticleScopeInline,]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['tag', ]

