from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    nickname = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.name}'