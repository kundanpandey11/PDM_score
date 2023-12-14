from django.db import models


class score(models.Model):
    #weights 
    w1 = models.FloatField(null=True,blank=True)
    w2 = models.FloatField(null=True,blank=True)
    w3 = models.FloatField(null=True,blank=True)
    nsr = models.FloatField(null=True, blank=True)
    rb = models.FloatField(null=True, blank=True)
    sensitivity = models.FloatField(null=True, blank=True)
    pdm_score = models.FloatField(null=False,blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.created_datetime} | {self.pdm_score}"
        