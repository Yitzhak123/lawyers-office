from django.conf.urls import include, url
from django.contrib import admin

import django.contrib.auth.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout,
        name='logout', kwargs={'next_page': '/lawyers_office/'}),
    url(r'^lawyers_office/', include('lawyers_office.urls')),
]