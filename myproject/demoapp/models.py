from django.db import models

# Create your models here.


class Villa(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    price = models.TextField()

    def __str__(self):
        return self.name