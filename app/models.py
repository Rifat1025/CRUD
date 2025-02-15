from django.db import models

class Crud(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=[
        ('user', 'User'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
    ])
    def __str__(self):
        return self.name
