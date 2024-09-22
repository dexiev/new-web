# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes





# views.py
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({"message": "Logged out successfully"}, status=200)
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)





from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Profile

@api_view(["POST"])
def registrationAPI(request):
    if request.method == "POST":
        username = request.data.get("username")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password1 = request.data.get("password1")
        password2 = request.data.get("password2")
        referral_code = request.data.get("referral_code", None)  # referral code is optional

        if User.objects.filter(username=username).exists():
            return Response({"error": "A user with that username already exists"})
        
        if password1 != password2:
            return Response({"error": "Passwords do not match"})

        # Create a new user
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True
        )
        user.set_password(password1)
        user.save()

        # Handle referral code if provided
        if referral_code:
            try:
                referrer_profile = Profile.objects.get(code=referral_code)
                user.profile.recommended_by = referrer_profile
                user.profile.save()
            except Profile.DoesNotExist:
                return Response({"error": "Invalid referral code"}, status=400)

        return Response({"success": "User successfully registered"})







#You can add an API for users to retrieve their own referral code.
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_referral_code(request):
    profile = request.user.profile
    return Response({"referral_code": profile.code})










from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response

@api_view(['POST'])
def logout_view(request):
    try:
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=400)

        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=205)
    except Exception as e:
        return Response({'error': str(e)}, status=400)




class LoginView(TokenObtainPairView):
    pass

