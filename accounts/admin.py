from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserRegistrationForm
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    form=UserRegistrationForm
    list_display = ('email','full_name','phone_number','is_admin',)
    list_filter = ('full_name',)
    ordering = ('email',)
    search_fields = ('full_name',)
    filter_horizontal = ()




admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

