from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('user_info/',views.user_info,name='user_info'),
    path('logout/',views.logout,name='logout'),
    path('login_for_medal/',views.login_for_medal,name='login_for_medal'),
    path('register/',views.register,name='register'),
]
