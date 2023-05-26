from django.db import models

# # Create your models here.
class crudUser(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    email = models.EmailField()
    # password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname

    def fullname(self):
        return self.firstname + " " + self.lastname


class deleteModel(models.Model):
    yes = models.BooleanField(default=False)
    no = models.BooleanField(default=False)