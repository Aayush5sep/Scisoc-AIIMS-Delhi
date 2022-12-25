from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.frontpage),
    path('register/<uuid:qid>',views.register_quiz),
    path('livequiz/<uuid:qid>',views.live_quiz),
    path('submit/<uuid:qid>',views.submit_quiz),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
