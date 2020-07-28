from rest_framework import serializers
from django.contrib.auth.models import User


from . models import Post, Category


''' 
Nested Serializer for Categories and User
'''

# For showing user Property
class UserSerializer_1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# For showing post on category
class PostSerializer_1(serializers.ModelSerializer):
	owner = UserSerializer_1(many=False, read_only=True) # for nested link getting user all property
	
	class Meta:
		model = Post
		fields = ['id','title','body','owner']





class CategorySerializer(serializers.ModelSerializer):
	posts = PostSerializer_1(many=True, read_only=True, source='post_set') # for nested link getting all post under category
	
	class Meta:
		model = Category
		fields = ['id','title','posts','created_at']



class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	url = serializers.HyperlinkedIdentityField(view_name='single-post')


	# category = serializers.StringRelatedField(many=False) #for categroy name
	# category = serializers.PrimaryKeyRelatedField(many=False, read_only=True)  # for categroy id
	# category = serializers.HyperlinkedRelatedField(
 #        many=False,
 #        read_only=True,
 #        view_name='single-category'
 #    )  # for categroy link


	class Meta:
		model = Post
		fields = ['id','url','title','body','category','owner','created_at']



class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all()) # it shwos post id
    posts = PostSerializer_1(many=True, read_only=True)  # shows all posts under a user

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']