from django.db import models


class MyBoard(models.Model):
    myname = models.CharField(max_length=30)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()

    def __str__(self):
        return str({'No': self.id})


class MyMember(models.Model):
    myname = models.CharField(max_length=100)
    mypassword = models.CharField(max_length=100)
    myemail = models.CharField(max_length=100)

    def __str__(self):
        return str({'myanme': self.myname, 'myemail': self.myemail})
