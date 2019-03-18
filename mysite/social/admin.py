from django.contrib import admin

from .models import Post, Org, OrgUser, ChatMessage, Chat


class PostDjangoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['post_text', 'user']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    readonly_fields = ('pub_date',)

    list_display = ('post_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['post_text']


class OrgDjangoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'picture', 'address']}),
    ]

    list_display = ('name', 'address')
    list_filter = ['name']
    search_fields = ['name']


class OrgUserDjangoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_id', 'member_status', 'organisations', 'payment']}),
    ]

    readonly_fields = ('user_id',)

    list_display = ('user_id', 'member_status')
    list_filter = ['member_status', 'organisations']
    search_fields = ['user_id', 'organisations']


class ChatMessageDjangoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['org_user_id', 'message_text', 'timestamp']}),
    ]

    readonly_fields = ('timestamp',)

    list_display = ('org_user_id',)
    list_filter = ['timestamp']
    search_fields = ['org_user_id', 'message_text']


class ChatDjangoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['chat_messages']}),
    ]

    search_fields = ['chat_messages']


admin.site.register(Post, PostDjangoAdmin)
admin.site.register(Org, OrgDjangoAdmin)
admin.site.register(OrgUser, OrgUserDjangoAdmin)
admin.site.register(ChatMessage, ChatMessageDjangoAdmin)
admin.site.register(Chat, ChatDjangoAdmin)
