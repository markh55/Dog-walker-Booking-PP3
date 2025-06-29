"""
URL configuration for dogwalkerbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookings import views as bookings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('bookings/', include('bookings.urls')),
    path('', bookings_views.home_view, name='home'),


]

from django.views.static import serve
from django.conf import settings
import os

urlpatterns += [
    path(
        "google6cC0gzeNqpXBJv51P3XsFicX5dp3y-gFP6o1kYiEqXU.html",
        serve,
        {
            "path": "google6cC0gzeNqpXBJv51P3XsFicX5dp3y-gFP6o1kYiEqXU.html",
            "document_root": os.path.join(settings.BASE_DIR, "static"),
        },
    ),
]

