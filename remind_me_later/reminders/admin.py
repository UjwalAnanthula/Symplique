from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('message', 'delivery_date', 'delivery_time', 'delivery_method', 'created_at')
    list_filter = ('delivery_method', 'delivery_date')
    search_fields = ('message',)