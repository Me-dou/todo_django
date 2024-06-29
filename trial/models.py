from django.db import models

class Todo(models.Model):
    titles = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    isCompleted = models.BooleanField(default=False)
    
    def __str__(self): 
        return f"{self.titles}({'Completed'  if self.isCompleted else 'Not Completed'})"
    
    

