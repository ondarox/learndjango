"""proj123 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^app123/', include('app123.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
	
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#static.static(view=django.views.static.serve)
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
	

#if settings.DEBUG:
    # static files (images, css, javascript, etc.)
 #   urlpatterns += patterns('',(r'^app123/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))