from django.db import models

from ckeditor.fields import RichTextField


class Main(models.Model):
    title = models.CharField(max_length=250)
    website = models.CharField(max_length=1000)
    description = RichTextField(blank=True)