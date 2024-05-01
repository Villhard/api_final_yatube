from posts.models import Comment, Follow, Group, Post
from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    actions = ("delete_selected",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "created", "author")
    actions = ("delete_selected",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    actions = ("delete_selected",)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "following")
    actions = ("delete_selected",)
