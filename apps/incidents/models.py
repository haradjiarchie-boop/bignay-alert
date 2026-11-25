
from django.conf import settings
from django.db import models


class Incident(models.Model):

    # Types of emergencies that residents can report
    INCIDENT_TYPES = [
        ('FIRE', 'Fire'),
        ('MEDICAL', 'Medical Emergency'),
        ('CRIME', 'Crime'),
        ('ROAD_ACCIDENT', 'Road Accident'),
        ('FLOOD', 'Flood'),
        ('OTHER', 'Other'),
    ]

    # Incident processing statuses
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('UNDER_REVIEW', 'Under Review'),
        ('VERIFIED', 'Verified'),
        ('ASSIGNED', 'Assigned'),
        ('ACCEPTED', 'Accepted'),
        ('EN_ROUTE', 'En Route'),
        ('ARRIVED', 'Arrived'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    # Resident who reported the incident
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='reported_incidents'
    )

    # Emergency information
    incident_type = models.CharField(
        max_length=30,
        choices=INCIDENT_TYPES
    )

    description = models.TextField()

    # Location information
    location = models.CharField(max_length=255)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    # Incident processing information
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SUBMITTED'
    )

    cancellation_reason = models.TextField(
        blank=True,
        default=''
    )

    # Automatic timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_incident_type_display()} - {self.status}"
