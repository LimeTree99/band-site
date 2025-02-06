from django.db import models

class Gig(models.Model):
    #this is a table
    venue =  models.CharField(max_length = 140, default='')
    location = models.CharField(max_length = 140, default='')
    date = models.DateTimeField()



    def __str__(self):
        return '{} {} {}'.format(self.venue, self.location, self.date.date().strftime('%b %d, %Y'))
