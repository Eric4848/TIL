from django.db import models
from django.conf import settings

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=30)
    autho = models.CharField(max_length=50)
    imagefile = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.title)
