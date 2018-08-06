from django.urls import path,re_path,include
from hybapp import views

app_name='hybapp'
urlpatterns = [
    path('hybridization/', views.hybridization),
    path('hybresult/', views.hybresult),
    path('hybinfolist/', views.hybinfolist),
    path('hybinfolist/<int:pageindex>/', views.hybinfolist),
    re_path('hybinfo_(\d+)/$', views.hybinfo),
    path('hybrecord/', views.hybrecord),

]