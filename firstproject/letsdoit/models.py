from django.db import models

class Myinfo(models.Model):
    SEX=[('f','female'),('m','male')]
    name=models.CharField(max_length=100)
    age= models.CharField(max_length=100)
    gender= models.CharField(choices=SEX,max_length=1,blank=True)
    submission=models.DateField()
    myjob=models.ManyToManyField('Myjob',blank=True)
class Myjob(models.Model):
    name=models.CharField(max_length=50)    
    
    def __str__(self):
        return self.name

 