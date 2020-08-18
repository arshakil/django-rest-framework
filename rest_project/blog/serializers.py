from rest_framework import serializers
from .models import User, UserProfile, Category, Post


# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):

		class Meta:
			model = UserProfile
			fields = ['user', 'gender']


# CategoriesSerializer 
class CategoriesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ['category_name',]

# Post serializer
class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ['title','description']


class RegisterSerializer(serializers.ModelSerializer):
	category = CategoriesSerializer(write_only=True)
	post = PostSerializer(write_only=True)
	password = serializers.CharField(max_length=68, min_length=6, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password','category','post']

	def validate(self, attrs):

		email = attrs.get('email', '')
		username = attrs.get('username', '')

		if not username.isalnum():
			raise serializers.ValidationError(
			'The username should only contain alphanumeric characters')
		return attrs

# Create Method
	def create(self, validated_data):
		print("data in serializer:: ", validated_data)

		blog_category = validated_data.pop('category')
		blog_post = validated_data.pop('post')

		user = User.objects.create_user(**validated_data)

		cat = Category.objects.create(
		category_name=blog_category["category_name"],
		)
		post = Post.objects.create(
		title=blog_post["title"],
		category=cat,
		author=user,
		description=blog_post["description"]
		)
		return validated_data


		# return User.objects.create_user(**validated_data)
