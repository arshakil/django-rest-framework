from django.contrib import admin

# Register your models here.


from .models import User
from . models import Post, Category, UserProfile, Region, Continent

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
# admin.site.register(UserProfile)

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

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id',)
admin.site.register(UserProfile, UserProfileAdmin)

# region and continent
admin.site.register(Region)
admin.site.register(Continent)