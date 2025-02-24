from django.db import models

class Assessor(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    certification_id = models.CharField(max_length=50, blank=True, null=True)

class AssessmentMethod(models.Model):
    method_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Assessment(models.Model):
    category = models.CharField(max_length=50)
    score = models.FloatField()
    method = models.ForeignKey(AssessmentMethod, on_delete=models.CASCADE)
    assessor = models.ForeignKey(Assessor, on_delete=models.CASCADE)

class EnergySystem(models.Model):
    system_type = models.CharField(max_length=50)
    efficiency_score = models.FloatField()

class SRILevel(models.Model):
    level_name = models.CharField(max_length=50)
    description = models.TextField()

class Building(models.Model):
    building_id = models.CharField(max_length=50, unique=True)
    geometry = models.TextField()  # GML als String
    sri_level = models.ForeignKey(SRILevel, on_delete=models.CASCADE)
    assessments = models.ManyToManyField(Assessment)
    energy_systems = models.ManyToManyField(EnergySystem)
