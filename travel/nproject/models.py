from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(default="name",max_length=255)
    des=models.TextField(default="Mo")
    img=models.ImageField(upload_to='pic')

    def __str__(self):

        return self.name
class staff(models.Model):
    name=models.CharField(max_length=255)
    post=models.TextField(default="")
    img=models.ImageField(upload_to='pic')



