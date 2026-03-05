from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MyHome, name='home'),
    path('pricing', views.Pricing, name='pricing'),
    path('auth/', include('UserAuth.urls')),
    path('blogs/', include('BlogDrafts.urls')),
]
