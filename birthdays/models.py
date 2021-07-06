from django.db import models

class Birthday(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='birthdays/images/', null=True, blank=True)

    def __str__(self):
        return str(self.id)
