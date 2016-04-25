from __future__ import unicode_literals

from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10, blank=True, db_index=True)

    @property
    def city_state_zip(self):
        return self.name + " " + self.state + ", " + self.zip_code

    class Meta:
        verbose_name_plural = "Cities"

    def __unicode__(self):
        return self.city_state_zip
