from django.db import models

# Create your models here.
class Employer(models.Model):
    title           = models.CharField(max_length=60)
    tel             = models.CharField(max_length=19,blank=True)
    fax             = models.CharField(max_length=19,blank=True)
    address         = models.TextField(blank=True)
    insurance_code  = models.TextField(max_length=20,blank=True)
    is_deleted      = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class EmployeeStatus(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.TextField(blank=True)

    def __str__(self):
        return self.title

class WorkStatus(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.TextField()

    def __str__(self):
        return self.title

class MaritalStatus(models.Model):
    title           = models.CharField(max_length=20)
    description     = models.TextField()

    def __str__(self):
        return self.title
    
class Bank(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.TextField()

    def __str__(self):
        return self.title


class WorkGroup(models.Model):
    title           = models.CharField(max_length=100)
    child_benefit   = models.DecimalField(max_digits=50,decimal_places=2)
    dwelling_benefit= models.DecimalField(max_digits=50,decimal_places=2)
    Bon_benefit     = models.DecimalField(max_digits=50,decimal_places=2)

    def __str__(self):
        return self.title

class WorkPlace(models.Model):
    title           = models.CharField(max_length=60)
    description     = models.TextField(blank=True)

    def __str__(self):
        return self.title


class PostPlace(models.Model):
    title           = models.CharField(max_length=60)
    decription      = models.TextField(blank=True)

    def __str__(self):
        return self.title



class Employee(models.Model):
    employer        = models.ForeignKey(Employer,on_delete=models.DO_NOTHING)
    firstname       = models.CharField(max_length=50)
    lastname        = models.CharField(max_length=50)
    fathername      = models.CharField(max_length=50)
    national_code   = models.CharField(max_length=10)
    id_number       = models.CharField(max_length=10)
    insurance_id    = models.CharField(max_length=10)
    employee_status = models.ForeignKey(EmployeeStatus,on_delete=models.DO_NOTHING)
    work_place      = models.ForeignKey(WorkPlace,on_delete=models.SET_NULL,null=True)
    post_place      = models.ForeignKey(PostPlace,on_delete=models.SET_NULL,null=True)
    work_status     = models.ForeignKey(WorkStatus,on_delete=models.PROTECT)
    marital_status  = models.ForeignKey(MaritalStatus,on_delete=models.DO_NOTHING)
    children_count  = models.IntegerField()
    work_group      = models.ForeignKey(WorkGroup,on_delete=models.SET_NULL,null=True)
    work_place      = models.ForeignKey(WorkPlace,on_delete=models.SET_NULL,null=True)
    tax_exempt      = models.BooleanField(default=False)
    indsurence_exempt= models.BooleanField(default=False)
    tel             = models.CharField(max_length=19,blank=True)
    mobile          = models.CharField(max_length=19,blank=True)
    description     = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.lastname,self.firstname,self.national_code)


class BankAccount(models.Model):
    employee        = models.ForeignKey(Employee,on_delete=models.CASCADE)
    account_number  = models.CharField(max_length=30)
    bank            = models.ForeignKey(Bank,on_delete=models.DO_NOTHING)
    is_active       = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.employee,self.account_number)
