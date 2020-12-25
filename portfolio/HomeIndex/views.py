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
    project_list = [project for project in projects] # get the list of projects. 
    context['project_list'] = project_list # add the project list in the context of project list. 
    return render(request, 'HomeIndex/HomeIndex.projects.html', context) # responce 

 