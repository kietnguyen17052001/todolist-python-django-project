from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255, null = True)
    def __str__(self):
        return f"{self.name}({self.id})"
    
class Task(models.Model):
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE, 
                             null=True, blank=True)
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255, null = True)
    createdAt = models.DateTimeFieldTextField(auto_now_add=True)
    updatedAt = models.DateTimeFieldTextField(auto_now=True)
    complete = models.BooleanField(default=False)
    category = models.ForeignKey(Category, 
                                   on_delete=models.CASCADE, 
                                   blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}({self.id})"
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
