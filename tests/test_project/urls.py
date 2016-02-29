from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()  # django < 1.7 support

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^advanced_filters/', include('advanced_filters.urls'))
)
