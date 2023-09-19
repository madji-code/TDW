"""
URL configuration for object3d project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-admin/', include('auth_admin.urls')),
    path('sale-point/', include('sale_point.urls')),
    # path('open-source/', include('open_source.urls')),
    # path('open-space-learning/', include('opsl.urls')),
    path('', include('mpaf.urls')),

]

handler404 = "auth_admin.views.error_404"