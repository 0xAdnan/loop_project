from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusTimeStampt(TimeStampMixin):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    timestamp_utc = models.DateTimeField()
    store_status = models.BooleanField(default=True)


class BusinessHoursTime(TimeStampMixin):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    day_of_week = models.IntegerField()
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()


class TimezonesDetails(TimeStampMixin):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    timezone_str = models.CharField(max_length=50)



