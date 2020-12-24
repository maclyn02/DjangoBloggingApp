from django.utils import timezone
from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Create string representation -> when you try to print a class, it will print the title instead
    def __str__(self):
        return str(f"{self.title} by {self.author}")


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return str(f"{self.text}")

    def like(self):
        self.likes = self.likes + 1

    def dislike(self):
        self.dislikes = self.dislikes + 1
