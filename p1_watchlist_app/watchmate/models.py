from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=40)
    active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.description}"
    
    class Meta:
        verbose_name_plural = "Movie"