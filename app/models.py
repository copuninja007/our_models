from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpages(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name  

class arrRrcordcce(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    data=models.DateField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.author