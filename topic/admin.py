from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Topic, Redactor, Newspaper


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_date", "topic")
    list_filter = ("publish_date", "topic")
    search_fields = ("title", "content")


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )


admin.site.register(Topic)
