from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = "users"
    iduser = models.AutoField("iduser", primary_key=true)    
    username = models.CharField("username", max_length=50)
    password = models.CharField("password", max_length=100)

    def __str__(self):
        return self.name
