from django.db import models
from views_generator import ViewGenerator
# Create your models here.
class Employer(models.Model):
    title           = models.CharField(max_length=60,verbose_name=u"عنوان")
    tel             = models.CharField(max_length=19,blank=True,verbose_name=u"تلفن")
    fax             = models.CharField(max_length=19,blank=True,verbose_name=u"فکس")
    address         = models.TextField(blank=True,verbose_name=u"آدرس")
    insurance_code  = models.TextField(max_length=20,blank=True,verbose_name=u"کد کارگاهی")
    is_deleted      = models.BooleanField(default=False,verbose_name=u"حذف شده")

    def __str__(self):
        return self.title

class EmployeeStatus(models.Model):
    title           = models.CharField(max_length=50,verbose_name=u"وضعیت پرسنل")
    description     = models.TextField(blank=True,verbose_name=u"توضیحات")
    def __str__(self):
        return self.title

class WorkStatus(models.Model):
    title           = models.CharField(max_length=50,verbose_name=u"عنوان وضعیت شغلی")
    description     = models.TextField(verbose_name=u"توضیحات")

    def __str__(self):
        return self.title

class MaritalStatus(models.Model):
    title           = models.CharField(max_length=20,verbose_name=u"وضعیت تاهل")
    description     = models.TextField(verbose_name=u"توضیحات")

    def __str__(self):
        return self.title
    
class Bank(models.Model):
    title           = models.CharField(max_length=50,verbose_name=u"نام بانک")
    description     = models.TextField(verbose_name=u"توضیحات")

    def __str__(self):
        return self.title


class WorkGroup(models.Model):
    title           = models.CharField(max_length=100,verbose_name=u"عنوان گروه")
    child_benefit   = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"مبلغ حق اولاد")
    dwelling_benefit= models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"مبلغ حق مسکن")
    Bon_benefit     = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"مبلغ بن")

    def __str__(self):
        return self.title

class WorkPlace(models.Model):
    title           = models.CharField(max_length=60,verbose_name=u"محل کار")
    description     = models.TextField(blank=True,verbose_name=u"توضیحات")

    def __str__(self):
        return self.title


class PostPlace(models.Model):
    title               = models.CharField(max_length=60,verbose_name=u"محل پست")
    number_of_employee  = models.IntegerField(verbose_name=u"تعداد کارکنان ")
    post_status         = models.ForeignKey(WorkStatus,on_delete=models.PROTECT,verbose_name=u"وضعیت پست")
    decription          = models.TextField(blank=True,verbose_name=u"توضیحات")

    def __str__(self):
        return self.title



class Employee(models.Model):
    employer        = models.ForeignKey(Employer,on_delete=models.DO_NOTHING,verbose_name=u"کارفرما")
    firstname       = models.CharField(max_length=50,verbose_name=u"نام")
    lastname        = models.CharField(max_length=50,verbose_name=u"نام خانوادگی")
    fathername      = models.CharField(max_length=50,verbose_name=u"نام پدر")
    national_code   = models.CharField(max_length=10,verbose_name=u"کد ملی")
    id_number       = models.CharField(max_length=10,verbose_name=u"شماره شناسنامه")
    insurance_id    = models.CharField(max_length=10,verbose_name=u"کد بیمه")
    employee_status = models.ForeignKey(EmployeeStatus,on_delete=models.DO_NOTHING,verbose_name=u"وضعیت")
    work_place      = models.ForeignKey(WorkPlace,on_delete=models.SET_NULL,null=True,verbose_name=u"محل کار")
    post_place      = models.ForeignKey(PostPlace,on_delete=models.SET_NULL,null=True,verbose_name=u"محل پست")
    work_status     = models.ForeignKey(WorkStatus,on_delete=models.PROTECT,verbose_name=u"وضعیت کاری")
    marital_status  = models.ForeignKey(MaritalStatus,on_delete=models.DO_NOTHING,verbose_name=u"وضعیت تاهل")
    children_count  = models.IntegerField(verbose_name=u"تعداد فرزند")
    work_group      = models.ForeignKey(WorkGroup,on_delete=models.SET_NULL,null=True,verbose_name=u"گروه")
    tax_exempt      = models.BooleanField(default=False,verbose_name=u"معافیت مالیاتی")
    indsurence_exempt= models.BooleanField(default=False,verbose_name=u"معافیت بیمه")
    tel             = models.CharField(max_length=19,blank=True,verbose_name=u"تلفن")
    mobile          = models.CharField(max_length=19,blank=True,verbose_name=u"موبایل")
    description     = models.TextField(blank=True,null=True,verbose_name=u"توضیحات")

    def __str__(self):
        return "{}-{}".format(self.lastname,self.firstname)


class BankAccount(models.Model):
    employee        = models.ForeignKey(Employee,on_delete=models.CASCADE,verbose_name=u"نام و نام خانوادگی")
    account_number  = models.CharField(max_length=30,verbose_name=u"شماره حساب")
    bank            = models.ForeignKey(Bank,on_delete=models.DO_NOTHING,verbose_name=u"نام بانک")
    is_active       = models.BooleanField(default=False,verbose_name=u"وضعیت")
    def __str__(self):
        return "{}-{}".format(self.employee,self.account_number)
