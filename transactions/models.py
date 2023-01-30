from django.db import models


class Transactions(models.Model):
    type = models.CharField(max_length=10)
    date = models.DateField()
    value = models.CharField(max_length=10)
    cpf = models.IntegerField()
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    def __str__(self) -> str:
        return f"{self.type} {self.value} {self.store_name}"
