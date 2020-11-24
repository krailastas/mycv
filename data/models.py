from django.db import models


class Main(models.Model):
    general_text = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128, blank=True)
    full_name = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.full_name


class Jobs(models.Model):
    place = models.CharField(max_length=256, blank=True)
    start = models.DateField(blank=True)
    end = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=True)
    company = models.CharField(max_length=128, blank=True)
    general_text = models.TextField(blank=True)

    def __str__(self):
        return self.company
