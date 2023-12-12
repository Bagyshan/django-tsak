from django.db import models
from author.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    date_of_print = models.DateTimeField()
    genre = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )


    def __str__(self):
        return f'{self.title}, {self.date_of_print}, {self.genre}, {self.author}'
    

# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     date_of_birth = models.DateTimeField()
#     nickname = models.CharField(max_length=5, blank=True)

#     def __str__(self):
#         return f'{self.name}'