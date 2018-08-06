from django.conf.urls import url
from django.urls import path,re_path,include
from . import views
app_name='userapp'
urlpatterns=[
    # path('', views.login),
    path('register/', views.register),
    path('registsave/', views.registsave),
    path('login/', views.login),
    path('logout/', views.logout),
    path('userexist/', views.userexist),

]