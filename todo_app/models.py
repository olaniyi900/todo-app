from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(null=True)

    def __str__(self):
        return self.name
    

