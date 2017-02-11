from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    dateOfBirth = models.DateField()
    def __unicode__(self):
        return self.user.username


class Payments(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    payed = models.BooleanField(default=False)
    due_date = models.DateField()
    amount = models.IntegerField()

    def __unicode__(self):
        if self.payed:
            return "%i payed on the %s", (self.amount, self.due_date)
        else:
            return "%i due on the %s",(self.amount,self.due_date)