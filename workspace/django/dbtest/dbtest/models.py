from django.db import models

class Myboard(models.Model): #Myboard : table
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()

    def __str__(self):
        return str({'myname':self.myname})