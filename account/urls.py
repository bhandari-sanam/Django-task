from django.urls import path
from account.views import UserLogoutView,UserLoginView, UserProfileView, UserRegistrationView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    path('logout/', UserLogoutView.as_view(), name='logout'),


]