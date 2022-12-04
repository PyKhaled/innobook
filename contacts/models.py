from django.db import models


LABEL_CHOICES = [
    ('mobile', "Mobile"),
    ('landline', 'Landline')
]


class Contact(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.numbers.first().dial}" if self.numbers.count() else self.name

    @property
    def primary_number(self):
        return self.numbers.first().dial if self.numbers.count() else None


class Number(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='numbers')
    label = models.CharField(max_length=50, choices=LABEL_CHOICES)
    dial = models.CharField(max_length=30)
