from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'find_us', 'news')
  list_display_links = ('id', 'name', 'email')
  search_fields = ('name', 'email')
  list_per_page = 25

# Register your models here.
admin.site.register(Message, MessageAdmin)