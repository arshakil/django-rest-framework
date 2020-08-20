from rest_framework import serializers
from .models import User, UserProfile, Category, Post


# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):

		class Meta:
			model = UserProfile
			fields = ['user', 'gender']
			# depth=2


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


# post list serializer
class UserListSerializer(serializers.ModelSerializer):
	# user_profile = UserProfileSerializer(many=False, read_only=True, source='user_profile_set')
	user_profile = UserProfileSerializer(many=False,read_only=True, source='user_profile.user')
	posts = PostSerializer(many=True, read_only=True, source='post_set')

	class Meta:
		model = User
		fields = ['id','username','email','posts','user_profile']




# Continent 
from .models import Continent, Region

class ContinentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Continent
        fields = [
            'id',
            'name',
            'description',
            'show',
        ]

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

# Region
class RegionSerializer(serializers.ModelSerializer):
    continent = ContinentListSerializer(many=False)

    def create(self, validated_data):
        continent_data = validated_data.pop('continent')
        validated_data['changed_by'] = self.context['request'].user.id
        continent_obj = super(ContinentListSerializer,ContinentListSerializer()).create(continent_data)
        validated_data['continent'] = continent_obj
        instance = super(self.__class__, self).create(validated_data)
        return instance

    def update(self, instance, validated_data):
        continent_data = validated_data.pop('continent')
        validated_data['changed_by'] = self.context['request'].user.id
        updated_obj = super(self.__class__, self).update(instance, validated_data)
        super(ContinentListSerializer, ContinentListSerializer()).update(instance.continent, continent_data)
        return updated_obj

    class Meta:
        model = Region
        fields = (
            'id',
            'name',
            'description',
            'show',
            'continent',
        )
        extra_kwargs = {
            'id': {
                "read_only": True
            }
        }


# for deropdown froeign key
class RegionNewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Region
		fields = (
		'id',
		'name',
		'description',
		'show',
		'continent',
		)
	    