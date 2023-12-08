from django.contrib import admin
from .models import Topic, Redactor, Newspaper


class NewspaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'topic')
    list_filter = ('publish_date', 'topic')
    search_fields = ('title', 'content')


admin.site.register(Topic)
admin.site.register(Redactor)
admin.site.register(Newspaper, NewspaperAdmin)
