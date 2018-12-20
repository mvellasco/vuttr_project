from django.db import models

class Tags(models.Model):
    """ Model representing the tags in a tool. """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """ Returns the name of the tag as it's string representation. """
        return self.name

class Tools(models.Model):
    """ Model representing a tool. """
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(max_length=500)
    tags = models.ManyToManyField("Tags")

    def __str__(self):
        """ Returns the title of a tool as it's string representation. """
        return self.title
