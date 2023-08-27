from django.urls import path
from .views import company_list, employee_list, device_list, device_log_list


urlpatterns = [
    path('api/companies/', company_list, name='api-company-list'),
    path('api/employees/', employee_list, name='api-employee-list'),
    path('api/devices/', device_list, name='api-device-list'),
    path('api/device-logs/', device_log_list, name='api-device-log-list'),
    # path('companies/add/', views.add_company, name='add_company'),
]