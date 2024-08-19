from django.db import models
from django.contrib.auth.models import User

class TopTips(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()  # Removed max_length
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ["-date_added"]
    
    def __str__(self):
        return self.title  # Simplified __str__ method