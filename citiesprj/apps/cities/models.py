from __future__ import unicode_literals

from django.db import models
from localflavor.us.models import USStateField, USZipCodeField


class City(models.Model):
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = USZipCodeField(blank=True, db_index=True)

    @property
    def city_state_zip(self):
        return self.city + " " + self.state + ", " + self.zip_code

    class Meta:
        verbose_name_plural = "Cities"

    def __unicode__(self):
        return self.city_state_zip
