"""
Definition of models.
"""

from django.db import models
import datetime
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.TextField(default='', blank=True)
    text_on_hover = models.TextField(default='', blank=True)
    published_date = models.CharField(max_length=100,default='', blank=True)
    additional_info = models.TextField(default='', blank=True)
    cartoon = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.id)