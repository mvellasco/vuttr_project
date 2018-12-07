from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tools(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(max_length=500)
    tags = models.ManyToManyField("Tags")

    def __str__(self):
        return self.title
