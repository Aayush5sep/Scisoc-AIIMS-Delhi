from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.edc),
    path('hackathon/<uid:uuid>',views.reg_hackathon),
    path('register/hackathon.<uid:uuid>',views.reg_hack),
    path('submit/hackathon.<uid:uuid>',views.submit_hack),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
