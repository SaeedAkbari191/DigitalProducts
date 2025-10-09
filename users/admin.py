from django.contrib import admin

from .models import User, Province, UserProfile


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

admin.site.register(Province)
admin.site.register(UserProfile)
