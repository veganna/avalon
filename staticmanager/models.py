from django.db import models


# Create your models here.

class staticManager(models.Model):


    keyobj = models.CharField(max_length=255, unique=True)
    type= models.IntegerField(default=1)
    textobj= models.CharField(max_length=255 ,default='' )
    textareaobj = models.TextField(default='' )
    fileobj = models.CharField(max_length=255, default='')
    linkobjh = models.CharField(max_length=255, default='')
    linkobjb = models.CharField(max_length=255, default='')

    def retType(self):
        if self.type == 1:
            return 'Text'
        if self.type == 2:
            return 'TextArea'
        if self.type == 3:
            return 'Image'
        if self.type == 4:
            return 'Link'
