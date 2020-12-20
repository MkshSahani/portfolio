from django.db import models

class Projects(models.Model): 


    auto_increment_id = models.AutoField(primary_key=True) #autoincrement id. 
    project_title = models.TextField(max_length=200) # title_of_projects. 
    programming_language_used = models.TextField(max_length=30) # text field.
    project_code_link = models.URLField() # url for the project field.  
    project_description = models.TextField() # a description about project. 


    def __str__(self): 
        return self.project_title # return the project title. 



