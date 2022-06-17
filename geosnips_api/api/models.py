from django.db import models

class geometry(models.Model):
    type = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=10000)
    def __str__(self):
        return self.type

class properties(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    ISO = models.CharField(max_length=100)
    state_code = models.CharField(max_length=100)
    id = models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.name

class features(models.Model):
    type = models.CharField(max_length=100)
    properties = models.ForeignKey(properties, on_delete=models.CASCADE)
    geometry = models.ForeignKey(geometry, on_delete=models.CASCADE)
    def __str__(self):
        return self.properties.id
