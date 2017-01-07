
from django.core.files import File
from django.db import models

# Create your models here.

class Music(models.Model):

    # def __init__(self, music_path):
    #     self.name = "TMP NAME"
    #     self.artist = "TMP ARTIST"
    #     self.music_file = File(open(music_path))

    name = models.CharField(max_length=1024, default="")
    artist = models.CharField(max_length=1024, default="")
    music_file = models.FileField(upload_to="mp3/")
