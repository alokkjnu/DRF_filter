from django.db import models

# Create your models here.

class ScoreCard(models.Model):
    Hand = models.IntegerField(default=False,blank=True)
    Card_Type= models.CharField(max_length=20, default=False, blank=True)
    Card_Value_Type = models.CharField(max_length=25,default=False,blank=True)
    Tricks = models.CharField(max_length=5,default=False,blank=True)
    Vulnerable = models.BooleanField(default=False,blank=True)
    Trick_Points = models.IntegerField(default=False,blank=True)

    def __str__(self):
        return self.Hand,self.Card_Type,self.Card_Value_Type,self.Tricks,self.Vulnerable,self.Trick_Points