from django.db import models

class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    doj = models.DateField()
    gender = models.CharField(max_length=10)
    designation = models.CharField(max_length=20)
    contactno = models.IntegerField()
    email = models.EmailField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="my_images",default=False)