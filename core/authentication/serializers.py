from rest_framework import serializers
from.models import CustomUser, Profile, ProfileType 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    last_login = serializers.CharField(required=True)
    profile_type = serializers.CharField(required=True, write_only = True)
    
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def create(self, validated_data):
        profile_type_name = validated_data.pop('profile_type')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        profile_type, created = ProfileType.objects.get_or_create(profile_type=profile_type_name)
        Profile.objects.create(user=user, profile_type=profile_type)

        return user