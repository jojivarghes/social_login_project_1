"""social_login_project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as site_views
from users import views as user_views

urlpatterns = [
    path(r'', site_views.home, name='home'),
    path(r'login', user_views.login, name='user_login'),
    path(r'logout', user_views.logout, name='user_logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('user/', include('users.urls')),
]
