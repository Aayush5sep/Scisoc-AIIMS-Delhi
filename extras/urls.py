from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('contact/',views.contactpage),
    path('sendprob/',views.contactreq),
    path('faqs/',views.faqs),
    path('announcement/',views.announce),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
