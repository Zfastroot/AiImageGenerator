"""
URL configuration for AiImageGenerator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from landingpage.views import index,about,team,demo,service,contact
from account.views import signin , signup , logout_user
from app.views import app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name='index'),
    path('about/', about , name='about'),
    path('service/', service , name='service'),
    path('team/', team , name='team'),
    path('demo/', demo , name='demo'),
    path('contact/', contact , name='contact'),
    path('signin/',signin ,  name='signin'),
    path('signup/',signup ,  name='signup'),
    path('logout/',logout_user ,  name='logout'),
    path('app/',app ,  name='app'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
