from django.db import models

class JobApplication(models.Model):
    STAGES = [
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('offer', 'Offer Received'),
        ('rejected', 'Rejected'),
    ]
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STAGES, default='applied')
    applied_on = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} - {self.position}"
