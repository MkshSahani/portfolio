# urls.py for homeIndex application. 
from django.urls import path

from . import views 

urlpatterns = [
    path('', views.homePageRender, name = "Home"), # render home page. 
    path('projects/', views.projectsPageRender, name="ProjectPage"), # render project page. 
         
]
