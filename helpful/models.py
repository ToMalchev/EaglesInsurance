from django.db import models
from embed_video.fields import EmbedVideoField


class helpful(models.Model):
    
    title = models.CharField(max_length=60, default='')
    text = models.TextField(default='')
    video = EmbedVideoField(default=None)
    


	
