from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.load_user_page, name='load_user_page'),
    url(r'^sign_up/$', views.add_new_user, name='add_new_user'),
    # url(r'^user/new/$', views.add_new_user, name='add_new_user'),
    # url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    # url(r'^user/(?P<pk>\d+)/remove', views.remove_user, name='remove_user'),
    # url(r'^(?P<app_type>\w+)/new/$', views.add_new_app, name='add_new_app'),
    # url(r'^(?P<app_type>\w+)/(?P<pk>\d+)/$', views.app_detail, name='app_detail'),
    # url(r'^(?P<app_type>\w+)/(?P<pk>\d+)/remove/$', views.remove_app, name='remove_app'),
]
