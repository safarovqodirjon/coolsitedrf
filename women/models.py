from django.db import models


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    photo = models.ImageField(upload_to="photos/", null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
