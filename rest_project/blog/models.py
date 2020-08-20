from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# for signal
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			username=username,
			password=password
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_verified				= models.BooleanField(default=False)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


# User Profile
GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('not_specified', 'Not Specified'),
)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=50,choices=GENDER_CHOICES, default='not_specified')
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Profile'
		verbose_name_plural = 'Profiles'

	def __str__(self):
		return self.user.username


# Category

class Category(models.Model):
	category_name = models.CharField(max_length=200)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'    

# Post
class Post(models.Model):
	title = models.CharField(max_length=5000)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author  = models.ForeignKey(User, on_delete=models.CASCADE)

	description = models.TextField()
	post_uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.title} - {self.category.category_name}'
	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts' 



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance, gender="male")

# Another way passing signal

# from django.db.models import signals
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		UserProfile.objects.create(user=instance)
# signals.post_save.connect(create_user_profile, sender=User, weak=False)



# Continent and region
class Continent(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    show = models.BooleanField(default=True)
    changed_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'continent'

class Region(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=255, null=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    show = models.BooleanField(default=True)
    changed_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'
        ordering = ['name']