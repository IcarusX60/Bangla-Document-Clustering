from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class Cluster(models.Model):
    cluster_no = models.IntegerField(default=0, unique=True)
    item_count = models.IntegerField(default = 0)
    news_type = models.CharField(max_length=200,null=True)

    def __int__(self):
        return self.cluster_no


class Article(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    headline = models.CharField(max_length = 200)
    content = models.CharField(max_length=2000,null=True, unique=True)

    def __str__(self):
        return self.headline

class Pcluster(models.Model):
    cluster_no = models.IntegerField(default=0, unique=True)
    item_count = models.IntegerField(default = 0)
    news_type = models.CharField(max_length=200,null=True)

    def __int__(self):
        return self.cluster_no


class Particle(models.Model):
    cluster = models.ForeignKey(Pcluster, on_delete=models.CASCADE)
    headline = models.CharField(max_length = 200, unique=True)
    content = models.CharField(max_length=2000,null=True, unique=True)

    def __str__(self):
        return self.headline