from django.db import models
from user.models import User

# Create your models here.
class RefferBy(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'reffer_by'

class Worker(models.Model):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    reffer_by = models.ForeignKey(RefferBy, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=10, null=True, blank=True)
    dl_image_front = models.TextField(null=True, blank=True)
    dl_image_back = models.TextField(null=True, blank=True)
    per_day_price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'worker'

class SubContractor(models.Model):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    business_name = models.CharField(max_length=500, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    trade_names = models.TextField(null=True, blank=True)
    license_no = models.TextField(null=True, blank=True)
    telephone_one = models.CharField(max_length=255, null=True, blank=True)
    telephone_two = models.CharField(max_length=255, null=True, blank=True)
    email_one = models.EmailField(null=True, blank=True)
    email_two = models.EmailField(null=True, blank=True)

    class Meta:
        db_table = 'sub_contractor'



class Customer(models.Model):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    telephone_one = models.CharField(max_length=255, null=True, blank=True)
    telephone_two = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        db_table = 'customer'

class Project(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    scope_of_works = models.TextField(null=True, blank=True)
    # contract = models.ForeignKey(Agreement, on_delete=models.CASCADE)
    profile_image = models.TextField(null=True, blank=True)    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    superintendent = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'project'


class Agreement(models.Model):
    sub_name = models.ForeignKey(SubContractor, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)    
    price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'agreement'

class Payment(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)
    check_no = models.TextField(null=True, blank=True)
    date = models.DateField(null=True)
    amount = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'payment'


class DailyWork(models.Model):
    date = models.DateField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, null=True, blank=True)
    invoice_number = models.TextField(null=True, blank=True)      
    receipt_image = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'daily_work'
        
class DailyWorker(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    work = models.ForeignKey(DailyWork, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'daily_worker'

class DailyWorkImage(models.Model):
    project_image = models.TextField(null=True, blank=True)    
    work = models.ForeignKey(DailyWork, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'daily_work_image'