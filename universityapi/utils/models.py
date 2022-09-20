from django.db import models
from django.contrib.auth import get_user_model


class AbstractTableMeta(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.DO_NOTHING,
                                   related_name='+')
    modified_by = models.ForeignKey(get_user_model(),
                                    on_delete=models.DO_NOTHING,
                                    related_name='+')

    class Meta:
        abstract = True

class WaitlistEntry(AbstractTableMeta, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    level = models.IntegerField(verbose_name='Class Level', default=1)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Waitlist entries'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Volunteer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    hours_available = models.TextField(blank=True, default='')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class VolunteerHours(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'VolunteerHours'