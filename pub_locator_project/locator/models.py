from django.core.validators import RegexValidator
from django.db import models


class PubInfo(models.Model):
    name = models.CharField(max_length=300)
    street_name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    suburb = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{0,4}$')])
    contact_number = models.CharField(max_length=10,
                                      validators=[RegexValidator(r'^\d{1,10}$')],
                                      blank=True,
                                      null=True
                                      )

    open_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
