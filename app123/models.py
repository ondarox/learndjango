from django.db import models


class Employee(models.Model):
	name=models.CharField(max_length=20);
	degree=models.CharField(max_length=20);
	
class Address(models.Model):
	employee=models.ForeignKey(Employee)
	houseno=models.CharField(max_length=20);
	city=models.CharField(max_length=20);
	
	
class Stuff(models.Model):
    numb = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    classio = models.CharField(max_length=1,null=True)
    #photo = models.ImageField(upload_to='')	
    photo = models.ImageField(upload_to='media')	
     	
# Create your models here.


class Aboutstuff(models.Model):
    stuff=models.OneToOneField(Stuff,null=True)
    aboutheading = models.CharField(max_length=255,null=True)
    abouttext = models.CharField(max_length=255,null=True)
    


class Review(models.Model):
    reviewtext = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media_review')	

	
class Comment(models.Model):
    commenttext = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media_comment')		