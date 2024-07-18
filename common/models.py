from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True ,blank=True, null=True)
    isDelete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True