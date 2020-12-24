from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse("blog:article-details", kwargs = {"id": self.id})
    
    def __str__(self):
        return self.title
