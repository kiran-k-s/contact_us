

from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('list_page',views.list_page, name='list_page'),
    path('detail',views.detail, name='detail'),
    path('home', views.index, name='index'),
    path('add', views.add, name='add'),
    path('', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('logout', views.logout_page, name='logout'),
    url(r'^api/contacts/$', views.contacts_list),
    url(r'^api/contacts/(?P<pk>[0-9]+)$', views.contacts_detail)
]
