from django.urls import path

from .api_views import EmployeeListAPIView, EmployeeByLevelAPIView


app_name = 'api'
urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='employees'),
    path('employee/<int:level>/', EmployeeByLevelAPIView.as_view(), name='employee'),
]
