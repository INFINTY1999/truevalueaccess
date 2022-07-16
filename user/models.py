from django.db import models

# Create your models here.

class users(models.Model):
    id = models.AutoField(unique=True,primary_key=True,editable=False)
    first_name = models.CharField(max_length=2000,null=True,blank=True)
    last_name = models.CharField(max_length=2000,null=True,blank=True)
    company_name = models.CharField(max_length=2000,null=True,blank=True)
    city = models.CharField(max_length=2000,null=True,blank=True)
    state = models.CharField(max_length=2000,null=True,blank=True)
    zip = models.IntegerField(default=0,null=True,blank=True)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    web = models.URLField(blank=True,max_length=128,db_index=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    
    def __str__(self) :
        return str(self.id)
    class Meta:
        ordering = ['id']
    
