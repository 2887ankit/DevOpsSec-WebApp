from django.urls import path 
from . import views 

app_name = 'plants'

urlpatterns = [ 
    path('', views.index, name='index'),
    path('<int:plant_id>/', views.show, name='show'),
    path('add_plant/', views.add_plant, name='add_plant'),
    ]