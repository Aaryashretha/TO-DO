from django.db import models

class Todo(models.Model):   #pascalcase projectwork
    title=models.CharField(max_length=200) #varchar,char



    def __str__(self):
        return self.title
    
