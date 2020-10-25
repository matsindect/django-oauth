from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)