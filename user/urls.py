from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as user_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='user/logout.html'), name='logout'),
    path('register/', user_views.register, name='register')
]
