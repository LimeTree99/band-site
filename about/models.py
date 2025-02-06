from django.db import models

class page(models.Model):
    #this is a table
    about =  models.TextField()

    def __str__(self):
        return self.about[:50]