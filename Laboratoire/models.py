from django.db import models


class LabResearch(models.Model):
    id_lab = models.CharField(max_length=200, primary_key=True)
    prevision_meteo = models.TextField()

    class Meta:
        db_table = 'labora'
