from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_written = models.DateTimeField()

    owner = models.ForeignKey(
        USER_MODEL,
        related_name="notes",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title
