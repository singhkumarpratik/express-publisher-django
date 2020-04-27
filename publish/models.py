from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

class express_publish(models.Model):
    title=models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',unique=True)
    author=models.CharField(max_length=50)
    body=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title