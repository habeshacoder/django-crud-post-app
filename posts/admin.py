from django.contrib import admin

from .models import PostModel


# Register your models here.
@admin.register(PostModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ("title", "content")
    list_filter = ("created",)
