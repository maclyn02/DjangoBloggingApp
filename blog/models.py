from django.utils import timezone
from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Create string representation -> when you try to print a class, it will print the title instead
    def __str__(self):
        return str(f"{self.title} by {self.author}")
