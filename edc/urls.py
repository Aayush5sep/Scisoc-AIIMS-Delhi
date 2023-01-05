from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.edc),
    path('hackathon/<uid:uuid>',views.reg_hackathon),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
