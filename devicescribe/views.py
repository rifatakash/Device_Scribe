# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Company, Employee, Device, DeviceLog
# from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer

# @api_view(['GET'])
# def company_list(request):
#     companies = Company.objects.all()
#     serializer = CompanySerializer(companies, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def employee_list(request):
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def device_list(request):
#     devices = Device.objects.all()
#     serializer = DeviceSerializer(devices, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def device_log_list(request):
#     device_logs = DeviceLog.objects.all()
#     serializer = DeviceLogSerializer(device_logs, many=True)
#     return Response(serializer.data)
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from devicescribe.models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Use Token Authentication
@permission_classes([IsAuthenticated])  # Require authentication
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def device_list(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def device_log_list(request):
    device_logs = DeviceLog.objects.all()
    serializer = DeviceLogSerializer(device_logs, many=True)
    return Response(serializer.data)

