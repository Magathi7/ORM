from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    name=models.CharField(max_length=20)
    players_id=models.CharField(max_length=100)
    weight=models.IntegerField()
    age=models.IntegerField()
    members=models.CharField(max_length=20)

class footballplayerAdmin(admin.ModelAdmin):
    list_display=('name','players_id','weight','age','members')