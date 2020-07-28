from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User

# class AccountAdmin(admin.UserAdmin):
class UserAdmin(admin.ModelAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	list_display_links = ('username',)
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(User, UserAdmin)