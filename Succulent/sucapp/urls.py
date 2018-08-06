from django.conf.urls import url
from django.urls import path,re_path,include
from sucapp import views
#https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path
app_name='sucapp'
urlpatterns = [
    # path('', views.main),
    path('main/', views.main),
    path('index', views.index),
    path('top', views.top),
    path('left', views.left),
    path('handbook/', views.handbook),
    path('handbook/<int:currentpage>/', views.handbook),
    re_path('sucdetail_(\d+)/$', views.sucdetail),
    path('maintenance/', views.maintenance),
    path('maintenance/<int:pageindex>/', views.maintenance),
    re_path('maindetail_(\d+)/$', views.maindetail),
    path('mainedit', views.mainedit),
    path('editsave', views.editsave),
    path('getgenus', views.getgenus),
    path('ihandbook/', views.ihandbook),
    path('ihandbook/<int:currentpage>/', views.ihandbook),
    # re_path(r'^(?P<pIndex>[0-9]*)/$', views.handbook, name='pagTest'),
]