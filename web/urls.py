"""ecomv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
# from accounts.views import home
from webcrawler.views import delete, dell, home, save_home, update, hm, org_name, url_short, vd

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('webcrawler', ),
    # path('homeurl'),
    path('update/', update, name="update"),
    path('delete/', delete, name="delete"),
    path('', home, name="home"),
    path('dell', dell, name="dell"),
    path('save', save_home, name="save_home"),
    path('home/', hm, name="hm"),
    path('org_name', org_name, name="org_name"),
    path('url_short', url_short, name="url_short"),
    path('vd', vd, name="vd")

]
admin.site.site_header = "eCom Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "Welcome to eCom"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
