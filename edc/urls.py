from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.edc),
    path('hackathon/<uuid:uid>',views.hackathon),
    path('hackathon/register/<uuid:uid>',views.reg_hack),
    path('hackathon/submit/<uuid:uid>',views.submit_hack),
    path('bioworkshop/register/<uuid:uid>',views.reg_ws),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
