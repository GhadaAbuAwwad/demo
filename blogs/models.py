from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Post(models.Model):
    #Post (title, pub_date, content, is_published)
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)
    post_content=models.CharField(max_length=4000)
    is_published=models.BooleanField(default=False)

    def __str__(self):
        return self.post_content

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

