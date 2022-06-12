"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from driverlicense import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.urls import re_path 

urlpatterns = [
    path('admin/', admin.site.urls), # admin page
    path('',views.index, name="index" ), #initial page
    path('home',views.index, name="home" ), #initial page    
    path('search', views.search, name="search" ), #search page 
    path('allcars', views.allcars, name="allcars"), #all crss
    path('add-car', views.add_car,  name="add-car"), #adding method as form view   
    path('employeers', views.all, name="employeers"), # list view all    
    path('add-person', views.add_person, name ="add-person"),#adding person as form view     
    re_path(r'^item/(?P<pk>\d+)/$', views.detail, name='detail'), #detail view of employeer
    path('deletecar/<car_id>', views.deletecar, name = "deletecar"),  #deleting car from base 
    path('deleteper/<person_id>', views.deleteper, name = "deleteper"),  #deleting person from base     
    re_path(r'update_car/<(?P<pk>\d+)/$', views.update_car, name='update_car'), # update cars
    re_path(r'update_person/<(?P<pk>\d+)/$', views.update_person, name='update_person'), #updating employers
]

#for static files

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    #here wils asdjb
