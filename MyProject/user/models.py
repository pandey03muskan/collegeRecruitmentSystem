from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    contact=models.CharField(max_length=20)
    message=models.CharField(max_length=600)
    def __str__(self):
            return self.name
    #not mine




class companies(models.Model):
    cname=models.CharField(max_length=40)
    cpic=models.ImageField(upload_to='static/companies/',default="")
    cdate=models.DateField()
    curl = models.CharField(max_length=500)
    ccity=models.CharField(max_length=40)
    def __str__(self):
        return self.cname

class register(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    email=models.CharField(max_length=200)
    passwd=models.CharField(max_length=50)
    number=models.CharField(max_length=30)
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    course=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    resume=models.ImageField(upload_to='static/resume/',default="")
    picture=models.ImageField(upload_to='static/profile/',default="")
    def __str__(self):
        return  self.name
class vacancy(models.Model):
    cid=models.ForeignKey(companies,on_delete=models.CASCADE)
    jid=models.IntegerField()
    designation=models.CharField(max_length=200)
    vacant=models.CharField(max_length=10)
    desc=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    salary=models.CharField(max_length=100)
    clocation=models.CharField(max_length=40)
    ccompany=models.CharField(max_length=100)
    vdate=models.DateField()
    vpic=models.ImageField(upload_to='static/card/',default="")
    def __str__(self):
        return self.designation

class applyjob(models.Model):
    jid=models.IntegerField()
    sid=models.CharField(max_length=200)




# class registration(models.Model):
#     name=models.CharField(max_length=120)
#     number=models.CharField(max_length=20)
#     email=models.CharField(max_length=80)
#     passwd=models.CharField(max_length=180)
#     dob=models.CharField(max_length=120)
#     pro=models.ImageField(upload_to='static/profile/',default="")
# """class cmpdetails(models.Model):
#     cname=model.CharField(max_length=400)
#     clogo=models.ImageField(upload_to='static/company',default="")
#     city=models.CharField(max_length=300)
#     cdate=models.DateField()"""
# #added
# """
# class placement(models.Model):
#     pic=models.ImageField(upload_to='static/placement/',default="")
#     name=models.CharField(max_length=120)
#     company=models.CharField(max_length=120)"""



