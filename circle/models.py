from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('circle.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Like(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post_pk = models.IntegerField(null=True)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)

