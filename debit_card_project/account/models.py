from django.db import models
#from ..user.models import User


# Create your models here.
class Account(models.Model):
    #user_id = models.ForeignKey(User, backref="accounts")
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    open_date = models.DateField()
    limit = models.FloatField()


    def __str__(self):
        return self.balance, self.open_date, self.limit