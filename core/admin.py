from django.contrib import admin

# Register your models here.
from core.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('date', )
    


admin.site.register(Article, ArticleAdmin)
