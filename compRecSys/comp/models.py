from django.db import models

# Create your models here.


class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'Category:%s' % self.cname


class Comp(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    sponsor = models.CharField(max_length=100)
    level = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'Comp:%s' % self.name


class CompDetail(models.Model):
    cdimgurl = models.ImageField(upload_to='',default='')
    cdurl = models.CharField(max_length=100)
    comp = models.ForeignKey(Comp, on_delete=models.CASCADE)
