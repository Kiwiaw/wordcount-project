
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name= 'home'),
    path("count/",views.count,name = 'count'),
    path("info/",views.info,name = 'info'),
    path("heja", views.jaki, name ='jaki'),
    path("buka", views.zium, name ='zium'),

]
