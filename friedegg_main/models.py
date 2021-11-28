from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=2000)
    published_date = models.DateTimeField("date published")
    publisher_id = models.BigIntegerField()
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(hours=1)
    def is_post_public(self):
        return True
