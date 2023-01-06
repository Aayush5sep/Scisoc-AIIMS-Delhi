from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.insight_home),
    path('details/<int:id>',views.insight),
    path('workshop/register/',views.reg_ws),
    path('event/register/',views.reg_event),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
