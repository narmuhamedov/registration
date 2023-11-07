from django.db import models

class Link(models.Model):
    original_url = models.URLField(max_length=2000)
    short_url = models.URLField(max_length=50, unique=True, null=True)