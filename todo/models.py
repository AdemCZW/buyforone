from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Flight(models.Model):
    items_choices = (
        ('tops', '衣服'),('pants','褲子'),('shoes','鞋子'),('accessories','配件'),('maintenance','保養品'),('makeup','化妝品'),('supplemen','保健食品')
    )
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    items = models.CharField(max_length=20, choices=items_choices)
    fromname = models.CharField(max_length=10,null=True,)
    arrivalname = models.CharField(max_length=50,null=True,)
    pd_number = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100)
    finish = models.BooleanField(default=False,null=True,)
    pub_date = models.DateTimeField(null=True,auto_now=True)
    pd_content = RichTextField(blank=True, null=True)
    pd_weight = models.TextField(max_length=100,null=True,verbose_name = '重量')
    pd_profit = models.TextField(max_length=100,null=True,verbose_name = '數值')


class Todo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='name')
    finish = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now)


# Create your models here.  
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
 
    def __str__(self):
        return self.firstname + " " + self.lastname
  
    class Meta:  
        db_table = "web_member"


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    tel = models.IntegerField()
    password = models.CharField(max_length=20, blank=False, null=True)    


    