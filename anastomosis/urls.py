from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.frontpage),
    path('register/<uuid:qzid>',views.register_quiz),
    path('livequiz/<uuid:qzid>',views.live_quiz),
    path('submit/<uuid:qzid>',views.submit_quiz),
    path('marks/<uuid:qzid>',views.view_marks),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
