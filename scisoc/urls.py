"""scisoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('gallery/',views.gallery),
    path('user/',include('user.urls')),
    path('extra/',include('extras.urls')),
    path('anastomosis/',include('anastomosis.urls')),
    path('journal/',include('journalclub.urls')),
    path('medquiz/',include('medquiz.urls')),
    path('edc/',include('edc.urls')),
    path('insight/',include('insight.urls')),
    path('payment/',include('payment.urls')),
    path('aboutdev/',views.developers),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
