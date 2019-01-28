from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['post_text']}),
        (None, {'fields': ['user']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    readonly_fields = ('pub_date',)

    list_display = ('post_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['post_text']


admin.site.register(Post, PostAdmin)