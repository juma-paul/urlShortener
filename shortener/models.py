from django.db import models

# Create your models here.
class URL(models.Model):
    long_url = models.URLField(max_length=2048, null=True, blank=True)
    short_url = models.CharField(max_length=7, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url} -> {self.long_url}"
