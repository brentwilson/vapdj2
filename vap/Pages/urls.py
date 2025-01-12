from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('page/<slug:slug>/', views.page, name='contentpage')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)