from django.db import models


class Main(models.Model):
    general_text = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128, blank=True)
    full_name = models.CharField(max_length=128, blank=True, unique=True)
    photo = models.ImageField(upload_to='data/photo', null=True, blank=True)
    github = models.URLField(blank=True, null=True)
    own_site = models.URLField(blank=True, null=True)
    order = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-order']


class Jobs(models.Model):
    main = models.ForeignKey('data.Main', on_delete=models.CASCADE, null=True, blank=True, related_name='jobs')
    place = models.CharField(max_length=256, blank=True)
    start = models.DateField(blank=True)
    end = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=True)
    company = models.CharField(max_length=128, blank=True)
    general_text = models.TextField(blank=True)
    order = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return self.company

    class Meta:
        ordering = ['-order']


class Languages(models.Model):
    main = models.ForeignKey('data.Main', on_delete=models.CASCADE, null=True, blank=True, related_name='languages')
    title = models.CharField(max_length=258, blank=True)
    order = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-order']
