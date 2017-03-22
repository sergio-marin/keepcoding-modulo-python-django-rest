from django.db import models

class Task(models.Model):

    PENDING = "PEN"
    DONE = "DON"
    STATUSES = (
        (PENDING, "Pending"),
        (DONE, "Done")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=3, default=PENDING, choices=STATUSES)
    time_estimated = models.IntegerField(null=True)
    deadline = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # automáticamente añade la fecha de creacion
    modified_at = models.DateTimeField(auto_now=True)  # automáticamente actualiza la fecha al guardar

    def __str__(self):
        return self.name
