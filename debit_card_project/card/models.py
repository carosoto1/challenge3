from django.db import models
#from ..account import Account


# Create your models here.
class Card(models.Model):
    #account_id = models.ForeignKey(Account, backref="cards")
    name = models.CharField(max_length=150)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.name, self.cvv