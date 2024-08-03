from django.db import models
from django.urls import reverse


class Petitioner(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    nationality = models.CharField(max_length=20, default='Unknown')

    class Meta:
    
        ordering = ('name',)
        verbose_name = 'petitioner'
        verbose_name_plural = 'petitioners'
    
    def __str__(self):
    
        return self.name
    
    def get_absolute_url(self):
    
        return reverse('dataentry:detail', args=[self.id])

