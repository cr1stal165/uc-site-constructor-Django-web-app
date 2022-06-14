"""uc_site_constructor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.clickjacking import xframe_options_sameorigin

from constructor import views

urlpatterns = [
    path('', views.index, name="index"),
    path('take-color/', views.take_color, name="take_color"),
    path('take-images/', views.take_images, name="take_images"),
    path('take_info/', views.take_info, name="take_info"),
    path('final_page/', views.final_page, name="final_page"),
    path('uc1/', xframe_options_sameorigin(views.template_uc1), name="template_uc1"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
