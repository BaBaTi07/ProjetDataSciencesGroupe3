
from django.db import models

class Etablissement(models.Model):
    spw_id = models.CharField(max_length=255)
    type_etablissement = models.CharField(max_length=255)
    implementation = models.CharField(max_length=255)
    nom_etablissement = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bot = models.BooleanField(default=False)