from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_account = models.OneToOneField(User)
    dateOfBirth = models.DateField()
    status_options = (('da', "data entry"),
                      ('we', "waiting evidence"),
                      ('wp', "waiting payment"),
                      ('rp', "repayment"),
                      ('cc', "canceled"))
    status = models.CharField(max_length=2, choices=status_options)
    crn= models.IntegerField(unique=True)
    def __unicode__(self):
        return self.user.username


class Payments(models.Model):
    user = models.ForeignKey(UserProfile)
    paid = models.BooleanField(default=False)
    due_date = models.DateField()
    amount = models.IntegerField()

    def __unicode__(self):
        if self.paid:
            return "%s %s - %i paid on the %s" % (self.user.user_account.first_name,
                                                  self.user.user_account.last_name,
                                                  self.amount, self.due_date)
        else:
            return "%s %s - %i due on the %s" % (self.user.user_account.first_name,
                                                 self.user.user_account.last_name,
                                                 self.amount, self.due_date)
