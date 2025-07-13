from django.contrib import admin
from django.urls import path

from aaa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('aaa/', views.aaa),
    path('bbb/', views.bbb),
    path('ccc/', views.ccc),
]
