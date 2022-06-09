from django.contrib import admin

from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # TODO: Add username with 'text'
    list_display = ['text', 'get_username']
    list_filter = ['user']

    def get_username(self, obj):
        return obj.user.username
