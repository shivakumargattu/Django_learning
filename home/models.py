from django.db import models

class Home(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="home_Images/")
    
    def __str__(self):
        return self.title