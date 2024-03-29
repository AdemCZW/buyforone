"""djangotodo URL Configuration

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

from django.urls import path, include
from todo.views import index, sign_up, sign_in, log_out
from django.contrib.auth import views


from django.contrib import admin
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('index/', views.sign_in, name='Login'),
    path('register/', views.sign_up, name='Register'),
    path('login/', views.sign_in, name='Login'),
    path('logout/', views.log_out, name='Logout'),
    path('flight/', include('todo.urls')),

]
