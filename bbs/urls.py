from django.urls import path
from . import views

app_name    = "bbs"
urlpatterns = [ 
    path('', views.index, name="index"),
    path('trend', views.trend, name="trend"),
    
]

