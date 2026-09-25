from django.db import models

class Incident(models.Model):
    employee_name = models.CharField(max_length=200)
    description = models.TextField()
    incident_date = models.DateField()
    severity = models.CharField(max_length=50)

    def __str__(self):
        return self.employee_name