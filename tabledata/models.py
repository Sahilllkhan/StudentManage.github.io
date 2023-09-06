from django.db import models

# Create your models here.
class tabledata(models.Model):
    regno=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    btime=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='static/image',default="")
    fee=models.CharField(max_length=50)
    remfee=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class passouts(models.Model):
    regno=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    btime=models.CharField(max_length=50)
    photo=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    remfee=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class fee(models.Model):#wrong
    regno=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    def __str__(self):
        return self.name





class feetable(models.Model):
    regno=models.CharField(max_length=50)
    rem=models.CharField(max_length=50)
    totalfee=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    date=models.CharField(max_length=50)