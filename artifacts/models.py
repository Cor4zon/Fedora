from django.db import models


class Artifact(models.Model):
    name = models.CharField(max_length=80)
    shiny = models.BooleanField()

    def __str__(self):
        return str(self.name)
