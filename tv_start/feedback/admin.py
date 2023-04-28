from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message')

admin.site.register(Feedback, FeedbackAdmin)