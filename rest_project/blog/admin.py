from django.contrib import admin

# Register your models here.


from .models import User
from . models import Post, Category, UserProfile

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)

# class UserAdmin(admin.UserAdmin):
class UserAdmin(admin.ModelAdmin):
	list_display = ('id','email','username','date_joined', 'last_login', 'is_admin','is_staff')
	list_display_links = ('username',)
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(User, UserAdmin)