from django.db import models

class Book(models.Model):
    guest_name = models.CharField(max_length=50)
    head_count = models.IntegerField()

    def __str__(self):
        return self.guest_name