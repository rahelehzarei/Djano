from django.db import models
from datetime import date

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique= True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length=264, unique = True)
    url = models.URLField(unique= True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete= models.CASCADE)
    date = models.DateField(default = date.today)
    count= models.IntegerField(default = 0)


    def __str__(self):
        return str(self.date)

class Company(models.Model):
    name = models.CharField(max_length=264,unique=True)
    number_of_employees= models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):

    employee_name = models.CharField(max_length=264, unique= True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default= date.today)

    def __str__(self):
        return self.employee_name