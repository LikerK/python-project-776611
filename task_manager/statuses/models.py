from django.db import models
from django.utils.translation import gettext_lazy
# Create your models here.

MAX_LENGTH = 100

class Status(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
        verbose_name=gettext_lazy('Name')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=gettext_lazy('Date of create')
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = gettext_lazy('Status')
        ordering = ['id']
