from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsEnrolled
from .serializers import EmployeeSerializer, EmployeeDetailSerializer
from ..models import Employee


class EmployeeListAPIView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, IsEnrolled)

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeByLevelAPIView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, IsEnrolled)

    def get(self, request, level):
        employees = Employee.objects.filter(level=level)
        serializer = EmployeeDetailSerializer(employees, many=True)
        return Response(serializer.data)
