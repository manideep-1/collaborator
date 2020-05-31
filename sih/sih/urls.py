"""sih URL Configuration

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
from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index),
   path('register',views.register,name='register'),
   path('login',views.login,name='login'),
   path('logincompany',views.logincompany,name='logincompany'),
   path('loginclient',views.loginclient,name='loginclient'),
   path('torture',include('templates.urls')),
   path('developer',views.developer),
   path('client',views.client),
   path('company',views.company),  
   path('admin',admin.site.urls),
   path('afterreg',views.afterreg),
   path('loginclient',views.loginclient),
   path('logincompany',views.logincompany),
   path('registerclient',views.registerclient,name='registerclient'),
   path('registercompany',views.registercompany,name='registercompany'),
   path('afterlogincompany',views.afterlogincompany),
   path('afterloginclient',views.afterloginclient),
   path('afterlogindeveloper',views.afterlogindeveloper),
   path('aftercd',views.aftercd),
   path('aftercc',views.aftercc),
   path('notify',views.notify),
path('notifyclient',views.notifyclient),
path('test',views.test)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)