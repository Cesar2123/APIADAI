"""APICESAR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from api.views import Home, About, powerB, Signin, CheckOut, success, cancel, inicio_ses, form_verificacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('login/', inicio_ses, name='login'),
    path('signin/', Signin.as_view(), name='signin'),
    path('form/', form_verificacion, name='form'),
    path('dashboard/', powerB.as_view(), name='dashboard'),
    path('payment/', CheckOut, name='payment'),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success')
]


