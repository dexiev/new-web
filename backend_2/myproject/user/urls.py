from django.urls import path
from . import views


urlpatterns = [
    # path('user/token/', obtain_auth_token, name='obtain-auth-token'),
    # path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.logout_view, name='auth_logout'),
    path("login/", views.LoginView.as_view()),
    # path("logout/", views.logout),
    path("register/", views.registrationAPI),
    path("refer_code/", views.get_referral_code)

]


# urls.py


urlpatterns = [
    
]
