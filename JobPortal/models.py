from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from .validators import validate_file_extension
# Create your models he re.   

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    Location=models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.name
    


class UserWithRole(models.Model):
    category_choices=(
        ('Male','male'),
        ('Female','female'),
        ('Other','other'), 
    )
    role_choices =(
        ('admin','admin'),
        ('hr','hr'),
        ('candidate','candidate'),
    )
    username =models.CharField(max_length=200, unique=True, null=False)
    first_name=models.CharField(max_length=200, default="first name")
    last_name=models.CharField(max_length=200,default="last name")
    companyname =models.CharField(max_length=200, null=True)
    dob=models.DateField(default="dob")
    gender= models.CharField(max_length=200,choices=category_choices,default="select gender")
    mobile= models.CharField(max_length=10, unique=True,null=False)
    email= models.CharField(max_length=200, unique=True,null=False)
    password1=models.CharField(max_length=200, null=True)
    password2=models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,choices=role_choices)
    create_by = models.ForeignKey(User, null=True, default=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.username



class Candidates(models.Model):
    candidate_user = models.ForeignKey(UserWithRole, on_delete=models.CASCADE, verbose_name="Candidate Name")
    resume=models.FileField(upload_to="static/resume/",validators=[validate_file_extension])
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.candidate_user)
 
# class Hruser(models.Model):
    
#     username =models.CharField(max_length=200,null=True)
#     first_name=models.CharField(max_length=200,null=True)
#     last_name=models.CharField(max_length=200,null=True)
#     mobile= models.CharField(max_length=200,null=True)
#     email= models.CharField(max_length=200,null=True)
#     companyname = models.ForeignKey(Company,on_delete=models.CASCADE ,blank=True,null=True)

#     def __str__(self):
#         return self.username

# class Adminuser(models.Model):
       
#         category=(
#         ('Male','male'),
#         ('Female','female'),
#         ('Other','other'), 
#     )
#         username =models.CharField(max_length=200, unique=True, null=False)
#         first_name=models.CharField(max_length=200, default="first name")
#         last_name=models.CharField(max_length=200,default="last name")
#         companyname = models.ForeignKey(Company,on_delete=models.CASCADE ,blank=True,null=True)
#         gender= models.CharField(max_length=200,choices=category,default="select gender")
#         mobile= models.CharField(max_length=200, unique=True,null=False)
#         email= models.CharField(max_length=200, unique=True,null=False)
#         password=models.CharField(max_length=200, null=True)
        

#         def __str__(self):
#             return self.username