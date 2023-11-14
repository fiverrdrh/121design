import csv
import os
import time
import calendar
from rest_framework.views import APIView
from .serializers import *
from utils.common import *
from .models import Customer
# Create your views here.

class ReferenceBy(APIView):
    serializer_class = ReferenceSerializer

    def post(self, request):
        try:
            reference_serializer = self.serializer_class(data=request.data)
            if reference_serializer.is_valid():
                reference_serializer.save()
                return success_response(message="Reference added successfully")
            return error_response(message="Invalid data")
        except Exception as e:
            return error_response(message=str(e))
        
        
class ReferenceByList(APIView):
    serializer_class = ReferenceSerializer
    pagination_class = CustomPagination

    def get(self, request):
        try:
            reference = RefferBy.objects.all().order_by("-id")
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(reference, request)
            serializer_data = self.serializer_class(paginated_queryset, many=True).data
            return paginator.get_paginated_response(serializer_data)             
        except Exception as e:
            return error_response(message=str(e))
        
        
        
class WorkerAdd(APIView):
    serializer_class = WorkerSerializer

    def post(self, request):
        try:
            image_ls = []
            images_path_ls = []
            image_ls.append(request.FILES["dl_image_front"])
            image_ls.append(request.FILES["dl_image_back"])
            gmt = time.gmtime()
            ts = calendar.timegm(gmt)
            reference_to_save = {
                "name": request.data.get("refer_name"),
                "telephone":request.data.get("refer_telephone"),
                "address": request.data.get("refer_address")
            }
            reference_serializer = ReferenceSerializer(data=reference_to_save)
            if reference_serializer.is_valid():
                reference_serializer.save()
                images_path = "/".join(["public","images",str(ts)])
                os.makedirs(images_path)
                for i in range(len(image_ls)):
                    with open(images_path+"/"+image_ls[i].name, "wb") as file:
                        for chunk in image_ls[i].chunks():
                            file.write(chunk)
                        images_path_ls.append(images_path+"/"+image_ls[i].name)
                worker_to_save = {
                    "full_name": request.data.get("full_name"),
                    "telephone": request.data.get("telephone"),
                    "address": request.data.get("address"),
                    "skills": request.data.get("skills"),
                    "reffer_by": reference_serializer.data["id"],
                    "ssn": request.data.get("ssn"),
                    "dl_image_front": images_path_ls[0],
                    "dl_image_back": images_path_ls[1],
                    "per_day_price": request.data.get("per_day_price"),

                }
                worker_serializer = self.serializer_class(data=worker_to_save)
                if worker_serializer.is_valid():
                    worker_serializer.save()
                    return success_response(message="Worker added successfully")
            return error_response(message="Invalid data")
            
        except Exception as e:
            return error_response(message=str(e))

        
class AgreementList(APIView):
    serializer_class = AgreementSerializer
    pagination_class = CustomPagination

    def get(self, request):
        try:
            agreement = Agreement.objects.all().order_by("-id")
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(agreement, request)
            serializer_data = self.serializer_class(paginated_queryset, many=True).data
            return paginator.get_paginated_response(serializer_data)
        except Exception as e:
            return error_response(message=str(e))

class DailyWorkList(APIView):
    serializer_class = DailyWorkSerializer
    pagination_class = CustomPagination

    def get(self, request):
        try:
            dailywork = DailyWork.objects.all().order_by("-id")
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(dailywork, request)
            serializer_data = self.serializer_class(paginated_queryset, many=True).data
            return paginator.get_paginated_response(serializer_data)
        except Exception as e:
            return error_response(message=str(e))


class WorkerList(APIView):
    serializer_class = WorkerSerializer
    pagination_class = CustomPagination
    def get(self, request):
        try:
            worker  = Worker.objects.all().order_by("-id")
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(worker, request)
            serializer_data = self.serializer_class(paginated_queryset, many=True).data
            return paginator.get_paginated_response(serializer_data)             
        except Exception as e:
            return error_response(message=str(e))
        
        
class AgreementAdd(APIView):
    serializer_class = AgreementSerializer
    def post(self, request):
        try:
            payment_ls = []
            agreement_to_save = {
                "sub_name": request.data.get("sub_id"),
                "project":request.data.get("project_id"),
                "start_date": request.data.get("start_date"),
                "end_date": request.data.get("end_date"),
                "price":request.data.get("price")
            }
            agreement_serializer = self.serializer_class(data=agreement_to_save)
            if agreement_serializer.is_valid():
                agreement_serializer.save()
                for payment in request.data.get("payments"):
                    payment["agreement"] = agreement_serializer.data["id"]
                    payment_ls.append(payment)
                payment_serializer = PaymentSerializer(data=payment_ls, many=True)
                if payment_serializer.is_valid():
                    payment_serializer.save()
                    return success_response(message = "Record added successfully")
            return error_response(message="Invalid data")                
        except Exception as e:
            return error_response(message=str(e))
        
        
class CustomerAdd(APIView):
    serializer_class = CustomerSerializer
    def post(self, request):
        try:
            customer_serializer = self.serializer_class(data=request.data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return success_response(message = "Customer added successfully")
            return error_response(message="Invalid data")                
        except Exception as e:
            return error_response(message=str(e))
        
class CustomerList(APIView):
    serializer_class = CustomerSerializer
    pagination_class = CustomPagination
    def get(self, request):
        try:
            customer  = Customer.objects.all().order_by("-id")
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(customer, request)
            serializer_data = self.serializer_class(paginated_queryset, many=True).data
            return paginator.get_paginated_response(serializer_data)             
        except Exception as e:
            return error_response(message=str(e))
        
        
class SubContractorAdd(APIView):
    serializer_class = SubContractorSerializer
    def post(self, request):
        try:
            subcontractor_serializer = self.serializer_class(data=request.data)
            if subcontractor_serializer.is_valid():
                subcontractor_serializer.save()
                return success_response(message = "Record added successfully")
            return error_response(message="Invalid data")                
        except Exception as e:
            return error_response(message=str(e))
        
        
class SubContractorList(APIView):
    serializer_class = SubContractorSerializer
    pagination_class = CustomPagination
    def get(self, request):
        try:
            subcontractor  = SubContractor.objects.all().order_by("-id")
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(subcontractor, request)
            serializer_data = self.serializer_class(paginated_queryset, many=True).data
            return paginator.get_paginated_response(serializer_data)                 
        except Exception as e:
            return error_response(message=str(e))
        
        
class ProjectAdd(APIView):
    serializer_class = ProjectSerializer
    def post(self, request):
        try:
            project_to_save = {
                "name":request.data.get("name"),
                "address": request.data.get("address"),
                "scope_of_works": request.data.get("scope_of_works"),
                "customer": request.data.get("customer_id"),
                "superintendent": request.data.get("superintendent_id")
            }
            image = request.FILES['profile_image']
            gmt = time.gmtime()
            ts = calendar.timegm(gmt)
            path = "/".join(["public","images", str(ts)])
            os.makedirs(path, exist_ok=True)
            input_image_path = path + "/" +image.name
            with open(input_image_path, "wb") as file:
                for f in image.chunks():
                    file.write(f)
            project_to_save["profile_image"] = input_image_path
            project_serializer = self.serializer_class(data=project_to_save)
            if project_serializer.is_valid():
                project_serializer.save()
                return success_response(message = "Record added successfully")
            return error_response(message="Invalid data")                
        except Exception as e:
            return error_response(message=str(e))
        
        
class ProjectList(APIView):
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    def get(self, request):
        try:
            project  = Project.objects.all().order_by("-id")
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(project, request)
            serializer_data = self.serializer_class(paginated_queryset, many=True).data
            return paginator.get_paginated_response(serializer_data)                 
        except Exception as e:
            return error_response(message=str(e))


class DailyWorkAdd(APIView):
    serializer_class = DailyWorkSerializer

    def post(self, request):
        try:
            images_path_ls = []
            gmt = time.gmtime()
            ts = calendar.timegm(gmt)
            images_path = "/".join(["public", "images", str(ts)])
            os.makedirs(images_path)
            worker_ls = request.data.get("workers_ids").split(",")
            daily_workers = []
            daily_work_images = []
            daily_work_to_save = {
                "date": request.data.get("date"),
                "project": request.data.get("id"),
                "company_name": request.data.get("company_name"),
                "invoice_number": request.data.get("invoice_number")
            }
            daily_work_serializer = self.serializer_class(data=daily_work_to_save)
            if daily_work_serializer.is_valid():
                daily_work_serializer.save()
                for worker in worker_ls:
                    daily_workers.append({
                        "worker": worker,
                        "work": daily_work_serializer.data["id"]
                    })
                worker_serializer = DailyWorkerSerializer(data=daily_workers, many=True)
                if worker_serializer.is_valid():
                    worker_serializer.save()

                for image in request.FILES.getlist("images"):
                    with open(images_path+"/"+image.name, "wb") as file:
                        for chunk in image.chunks():
                            file.write(chunk)
                        images_path_ls.append(images_path+"/"+image.name)
                for path in images_path_ls:
                    daily_work_images.append({
                        "receipt_image": path,
                        "work": daily_work_serializer.data["id"]
                    })
                work_image_serializer = DailyWorkImageSerializer(data=daily_work_images, many=True)
                if work_image_serializer.is_valid():
                    work_image_serializer.save()
                    return success_response(message="Record added successfully")
            return error_response(message="Invalid data")
        except Exception as e:
            return error_response(message=str(e))


class WorkerPerProjectReport(APIView):
    serializer_class = WorkerPerProjectReportSerializer
    def get(self, request):
        try:
            dailywork = DailyWork.objects.all()
            serializer_data = self.serializer_class(dailywork, many=True).data
            dir_path = os.path.join(settings.BASE_DIR, "public", "reports")
            os.makedirs(dir_path, exist_ok=True)
            file_name = os.path.join("public/reports/", "workerperproject"+".csv")
            headers = ["Project", "Worker Count"]
            with open(file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for data in serializer_data:
                    writer.writerow([data["project"],data["worker_count"]])
            return success_response(data=file_name)
        except Exception as e:
            return error_response(message=str(e))
        
        
class WorkerReport(APIView):
    serializer_class = WorkerSerializer
    def get(self, request):
        try:
            worker = Worker.objects.all()
            serializer_data = self.serializer_class(worker, many=True).data
            dir_path = os.path.join(settings.BASE_DIR, "public", "reports")
            os.makedirs(dir_path, exist_ok=True)
            file_name = os.path.join("public/reports/", "worker"+".csv")
            headers = ["Full Name", "Telephone", "Address", "Skills", "Reference","SSN", "Per Day Price"]
            with open(file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for data in serializer_data:
                    writer.writerow([data["full_name"],data["telephone"],data["address"],data["skills"],data["reference"],data["ssn"],data["per_day_price"]])
            return success_response(data=file_name)
        except Exception as e:
            return error_response(message=str(e))
        
        
class ProjectReport(APIView):
    serializer_class = ProjectSerializer
    def get(self, request):
        try:
            project = Project.objects.all()
            serializer_data = self.serializer_class(project, many=True).data
            dir_path = os.path.join(settings.BASE_DIR, "public", "reports")
            os.makedirs(dir_path, exist_ok=True)
            file_name = os.path.join("public/reports/", "project"+".csv")
            headers = ["Name", "Address", "Scope of Work", "Customer","SuperIntendent"]
            with open(file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for data in serializer_data:
                    writer.writerow([data["name"],data["address"],data["scope_of_works"],data["customer_name"],data["superintendent_name"]])
            return success_response(data=file_name)
        except Exception as e:
            return error_response(message=str(e))
        
        
class DailyWorkReport(APIView):
    serializer_class = DailyWorkSerializer
    def get(self, request):
        try:
            dailywork = DailyWork.objects.all()
            serializer_data = self.serializer_class(dailywork, many=True).data
            dir_path = os.path.join(settings.BASE_DIR, "public", "reports")
            os.makedirs(dir_path, exist_ok=True)
            file_name = os.path.join("public/reports/", "dailywork"+".csv")
            headers = ["Date", "Project", "Company Name", "Invoice Number","Workers"]
            with open(file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for data in serializer_data:
                    writer.writerow([data["date"],data["project_name"],data["company_name"],data["invoice_number"],",".join(data["workers"])])
            return success_response(data=file_name)
        except Exception as e:
            return error_response(message=str(e))
        
class ProjectPaymentReport(APIView):
    serializer_class = AgreementSerializer
    def get(self, request):
        try:
            agreement = Agreement.objects.all()
            serializer_data = self.serializer_class(agreement, many=True).data
            dir_path = os.path.join(settings.BASE_DIR, "public", "reports")
            os.makedirs(dir_path, exist_ok=True)
            file_name = os.path.join("public/reports/", "payment"+".csv")
            headers = ["Project Name", "Payments"]
            with open(file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for data in serializer_data:
                    payments_ls = []
                    for payment in data["payment_records"]:
                        payments_ls.append("amount:"+payment["amount"])
                    payments = ",".join(payments_ls)
                    writer.writerow([data["project_name"],payments])
            return success_response(data=file_name)
        except Exception as e:
            return error_response(message=str(e))
        
class DashBoard(APIView):
    def get(self, request):
        try:
            workers = Worker.objects.all().count()
            customers = Customer.objects.all().count()
            projects = Project.objects.all().count()
            sub_contractors = SubContractor.objects.count()
            return success_response(data={
                "workers": workers,
                "customers": customers,
                "projects": projects,
                "sub_contractors":sub_contractors
            })
        except Exception as e:
            return error_response(message=str(e))