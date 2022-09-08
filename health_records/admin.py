from django.contrib import admin
from .models import UserProfile

# Register your models here.
# admin.site.register(UserProfile)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'date_of_birth', 'email', 'phone')
    ordering = ('last_name', 'first_name')
    # list_filter = ('last_name')
