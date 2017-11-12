from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # Include precious application's urls
    url(r'', include('precious.urls')),
]
