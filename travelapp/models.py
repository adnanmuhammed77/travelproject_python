from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField()
    desc=models.TextField()

    def __str__(self) -> str:
        return self.name
    
class team(models.Model):
     name=models.CharField(max_length=250)
     img=models.ImageField()
     title=models.CharField(max_length=250)
     def __str__(self) -> str:
        return self.name