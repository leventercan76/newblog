from django.contrib import admin

from .models import Article
# Register your models here.

#admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["titles","author","created_date"]
    list_display_links = ["titles","created_date"]
    search_fields = ["titles","content"]
    list_filter = ["created_date"]
    class Meta:
        model = Article