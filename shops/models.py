from django.db import models


Time_choice=(
    ('am','am'),
    ('pm','pm')
)
class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    open_time_week = models.CharField('opening time on week days', max_length=10)
    am_pm_ow = models.CharField('am/pm', max_length=10, choices=Time_choice, default='am')
    close_time_week = models.CharField('Closing time on week days', max_length=10)
    am_pm_cw = models.CharField('am/pm', max_length=10, choices=Time_choice, default='am')

    open_time_end = models.CharField('opening time on weekend days', max_length=10)
    am_pm_oe = models.CharField('am/pm', max_length=10, choices=Time_choice, default='am')
    close_time_end = models.CharField('Closing time on weekend days', max_length=10)
    am_pm_ce = models.CharField('am/pm', max_length=10, choices=Time_choice, default='am')

    def __str__(self):
        return self.name
