from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('curates/',views.curates_list),
    path('twcaos/',views.twcaos_list),
    path('fryums/',views.fryums_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
