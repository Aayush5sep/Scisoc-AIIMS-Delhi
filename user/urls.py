from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('loginpage/',views.loginpage),
    path('login/',views.login),
    path('newaccnt/',views.signup),
    path('newaccntpage/',views.signuppage),
    path('logout/',views.logout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
