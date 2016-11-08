from django.conf.urls import url
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^$', views.load_user_page, name='load_user_page'),
    url(r'^sign_up/$', views.add_new_user, name='add_new_user'),
    url(r'^menu_options/(?P<link_url>\w+)$', views.get_left_top_nav_links,
        name='get_left_top_nav_links'),
    # url(r'^comment_list/$', views.get_comment_list, name='comment_list'),
    url(r'^settings/$', views.load_settings_page, name='settings'),
    url(r'^info/$', views.load_info_page, name='info'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^open_file/$', views.open_file, name='open_file'),
    url(r'^reclassify/$', views.reclassify, name='reclassify'),
    url(r'^save_file/$', views.save_file, name='save_file'),
    url(r'^delete_file/$', views.delete_file, name='delete_file'),
    url(r'^more_options/$', views.more_options, name='more_options'),


    # url(r'^user/new/$', views.add_new_user, name='add_new_user'),
    # url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    # url(r'^user/(?P<pk>\d+)/remove', views.remove_user, name='remove_user'),
    # url(r'^(?P<app_type>\w+)/new/$', views.add_new_app, name='add_new_app'),
    # url(r'^(?P<app_type>\w+)/(?P<pk>\d+)/$', views.app_detail, name='app_detail'),
    # url(r'^(?P<app_type>\w+)/(?P<pk>\d+)/remove/$', views.remove_app, name='remove_app'),
]
