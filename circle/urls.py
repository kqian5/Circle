
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/new/$', views.post_new, name='post_new'),
    url(r'^posts/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^posts/(?P<pk>\d+)/delete/$', views.post_remove, name='post_remove'),
    url(r'^users/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^post/(?P<pk>\d+)/like/$', views.like, name='like'),
]
