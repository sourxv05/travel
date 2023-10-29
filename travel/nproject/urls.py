from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo,name='demo'),
    path('reg/', views.reg,name='reg'),
    path('log/', views.log,name='log'),
     path('logout/', views.logout,name='logout')




]
