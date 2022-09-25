from django.db import models

# Create your models here.
class CryptoCurrencyModel(models.Model):
    Name= models.CharField(max_length=100,null=False,blank=False)
    Price= models.CharField(max_length=100,null=False,blank=True)
    _1h = models.CharField(max_length=100,null=False,blank=True)
    _24h = models.CharField(max_length=100,null=False,blank=True)
    _7d=models.CharField(max_length=100,null=False,blank=True)
    market_cap= models.CharField(max_length=100,null=False,blank=True)
    volume=models.CharField(max_length=100,null=False,blank=True)
    circulating_supply=models.CharField(max_length=100,null=False,blank=True)

    def __str__(self):
        return self.Name
