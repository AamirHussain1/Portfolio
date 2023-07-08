from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)
    project_link = models.URLField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.project_name


