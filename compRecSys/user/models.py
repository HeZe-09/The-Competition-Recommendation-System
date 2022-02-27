from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.EmailField(max_length=100)
    pwd = models.CharField(max_length=100)

    def __unicode__(self):
        return u'UserInfo:%s'%self.uname