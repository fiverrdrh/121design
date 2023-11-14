from .models import *
from rest_framework import serializers
from construction_manager import settings

class ReferenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RefferBy
        fields = "__all__"
        
class WorkerSerializer(serializers.ModelSerializer):
    reference = serializers.SerializerMethodField("get_reference")
    
    class Meta:
        model = Worker
        fields = "__all__"

    def get_reference(self, obj):
        return obj.reffer_by.name


class AgreementSerializer(serializers.ModelSerializer):
    payment_records = serializers.SerializerMethodField("get_payment")
    subcontractor_name = serializers.SerializerMethodField("get_superintendent")
    project_name = serializers.SerializerMethodField("get_project")
    class Meta:
        model = Agreement
        fields = "__all__"

    def get_payment(self, obj):
        payment_ls = []
        payments = Payment.objects.filter(agreement_id=obj.id)
        if payments.exists():
            for payment in payments:
                payment_ls.append({
                    "check_no": payment.check_no,
                    "date": payment.date,
                    "amount": payment.amount
                })
            return payment_ls
        else:
            return payment_ls
        
    def get_superintendent(self, obj):
        if obj.sub_name is not None:
            return obj.sub_name.full_name
        else:
            return ""
        
    def get_project(self, obj):
        if obj.project is None:
            return ""
        else:
            return obj.project.name


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = "__all__"
        

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = "__all__"
        
        
class SubContractorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubContractor
        fields = "__all__"
        
        
class ProjectSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField("get_customer")
    superintendent_name = serializers.SerializerMethodField("get_superintendent")
    
    class Meta:
        model = Project
        fields = "__all__"
        
    def get_customer(self, obj):
        if obj.customer is not None:
            return obj.customer.full_name
        else:
            return ""           
        
    def get_superintendent(self, obj):
        if obj.superintendent is not None:
            return obj.superintendent.first_name +" "+ obj.superintendent.last_name
        else:
            return ""  

class DailyWorkSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField("get_image")
    workers = serializers.SerializerMethodField("get_worker")
    project_name = serializers.SerializerMethodField("get_project")

    class Meta:
        model = DailyWork
        fields = "__all__"

    def get_image(self, obj):
        image_ls = []
        images = DailyWorkImage.objects.filter(work=obj.id)
        if images.exists():
            for image in images:
                image_ls.append(image.project_image)
            return image_ls
        else:
            return image_ls

    def get_worker(self, obj):
        worker_ls = []
        workers = DailyWorker.objects.filter(work=obj.id)
        if workers.exists():
            for worker in workers:
                worker_ls.append(worker.worker.full_name)
            return worker_ls
        else:
            return worker_ls
    
    def get_project(self, obj):
        if obj.project is None:
            return ""
        else:
            return obj.project.name


class DailyWorkImageSerializer(serializers.ModelSerializer):


    class Meta:
        model = DailyWorkImage
        fields = "__all__"




class DailyWorkerSerializer(serializers.ModelSerializer):


    class Meta:
        model = DailyWorker
        fields = "__all__"


class DailyWorkerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWorkImage
        fields = "__all__"
        
        
class WorkerPerProjectReportSerializer(serializers.ModelSerializer):
    worker_count = serializers.SerializerMethodField("get_worker")
    project = serializers.SerializerMethodField("get_project")
    class Meta:
        model = DailyWork
        fields = ["project", "worker_count"]
        
    def get_project(self, obj):
        if obj.project is None:
            return ""
        else:
            return obj.project.name
        
    def get_worker(self, obj):
        dailyworker = DailyWorker.objects.filter(work=obj.id)
        if dailyworker.exists():
            return dailyworker.count()
        else:
            return ""