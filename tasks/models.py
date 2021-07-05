from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.user)

class Task (models.Model):

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False)
    duedate = models.DateTimeField(_("Duedate"), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

