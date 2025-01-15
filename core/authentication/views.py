from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .serializers import LoginSerializer, UserSerializer
from .models import ProfileType, Profile

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        
        user = authenticate(
            request, 
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password']
        )
        
        if user is not None:
            user.last_login = datetime.now()
            user.save()
            refresh = RefreshToken.for_user(user)
            
            user_serializer = UserSerializer(user)
            user_serializer = dict(user_serializer.data)
            user_serializer['refresh'] = str(refresh)
            user_serializer['access'] = str(refresh.access_token)
            
            return Response(user_serializer, status = status.HTTP_200_OK)
        else:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "The credentiales provided are not valid. Please review your information and try again"     
                },    
                status = status.HTTP_401_UNAUTHORIZED)
            
class SignUpView(APIView): 
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception= True)
        try:
            user, profile_type_selected = serializer.save()
            refresh, _ = RefreshToken.for_user(user)
            user_serialized = UserSerializer(user)
            user_serialized = dict(user_serialized.data)
            user_serialized['refresh'] = str(refresh)
            user_serialized['access'] = str(refresh.access_token)
            user_serialized['profile_type'] = str(profile_type_selected)
            profile_type = ProfileType.objects.get(pk = profile_type_selected)
            profile = Profile.objects.create(user=user, profile_type=profile_type)
            return Response(user_serialized, status = status.HTTP_200_OK)
        except:
            return Response(
                {
                    "error": "400 Bad Request",
                    "message": f"Email '{serializer.validated_data['email']}' is alredy registered"   
                },
                status= status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {
                "status": "200 ok", 
                "message": "You have successfully logged out"
                }
            )
        except Exception as e:
            return Response(
                {
                    "error": "400 Bad Request", 
                    "message": str(e)
                }, status = status.HTTP_401_UNAUTHORIZED
            )      