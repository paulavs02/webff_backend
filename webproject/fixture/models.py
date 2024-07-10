from django.db import models

# Create your models here.

class Escuadra(models.Model):
    equipo = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="escuadras")
    kills = models.IntegerField(default=0,  verbose_name = "Bajas")
    points = models.DecimalField(max_digits=5, decimal_places=2,  verbose_name = "Puntos")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.equipo
    
    class Meta:
        ordering = ['-points']