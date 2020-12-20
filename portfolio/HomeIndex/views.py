from django.shortcuts import render

from .models import Projects 


# To render the home page. 
def homePageRender(request): 
    context = {}

    return render(request, 'HomeIndex/HomeIndex.home.html', context) # responce.   


# To render the projects page. 
def projectsPageRender(request):
    # fetch the list of all projects. 
    context = {} # feed data need to send in it. 
    projects = Projects.objects.all() # get all projects 

    return render(request, 'HomeIndex/HomeIndex.projects.html', context) # responce 

