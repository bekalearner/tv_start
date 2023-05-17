from django.contrib import admin
from users_app.models import User

# admin.site.register(User)

@admin.register(User)
class User(admin.ModelAdmin):
    filter_horizontal = ['groups']