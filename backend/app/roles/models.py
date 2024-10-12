from django.db import models

class Rol(models.Model):
    nombre = models.CharField("Nombre", max_length=50, unique=True)

    def __str__(self):
        return self.nombre