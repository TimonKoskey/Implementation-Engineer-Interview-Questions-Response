from django.db import models

class AppContent(models.Model):
    content = models.CharField(max_length=50, blank=True, null=True)


contentModel = AppContent