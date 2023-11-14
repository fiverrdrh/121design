"""

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('refrence_add/', ReferenceBy.as_view()),
    path('refrence_list/', ReferenceByList.as_view()),
    path('worker_add/', WorkerAdd.as_view()),
    path('worker_list/', WorkerList.as_view()),
    path('worker_list/', WorkerList.as_view()),
    path('customer_add/', CustomerAdd.as_view()),
    path('customer_list/', CustomerList.as_view()),
    path('subcontractor_add/', SubContractorAdd.as_view()),
    path('subcontractor_list/', SubContractorList.as_view()),
    path('project_add/', ProjectAdd.as_view()),
    path('project_list/', ProjectList.as_view()),
    path('agreement_add/', AgreementAdd.as_view()),
    path('agreement_list/', AgreementList.as_view()),
    path('daily_work_add/', DailyWorkAdd.as_view()),
    path('dailywork_list/', DailyWorkList.as_view()),
    path('worker_per_project_report/', WorkerPerProjectReport.as_view()),
    path('worker_report/', WorkerReport.as_view()),
    path('project_report/', ProjectReport.as_view()),
    path('dailywork_report/', DailyWorkReport.as_view()),
    path('payment_report/', ProjectPaymentReport.as_view()),
    path('dashboard/', DashBoard.as_view()),
    # path('preview/', ImagePreviewSave.as_view()),
]