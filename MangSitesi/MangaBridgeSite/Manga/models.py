from datetime import datetime
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.core.files.storage import FileSystemStorage
import os
# Create your models here.

class Manga(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Manga", instance)

    MangaName = models.CharField(max_length=255)
    Thumbnail = models.ImageField(default = "default/noimage.png", upload_to = image_upload_to, max_length = 255)

    def __str__(self):
        return self.MangaName

class Chapter(models.Model):
    manga = models.ForeignKey(Manga,on_delete=models.CASCADE)
    url = models.URLField()
    Number = models.IntegerField()
    pub_date = models.DateTimeField(default=datetime.now())
    Translator = models.CharField(max_length=30)
    

