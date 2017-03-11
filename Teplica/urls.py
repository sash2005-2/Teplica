from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Teplica.views.home', name='home'),

    url(r'^', include('teplc.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
