from django.urls import path
from . import views
from rest_framework import permissions

app_name = 'nurses'

urlpatterns = [
    path('profile/', views.GetProfile.as_view(), name='profile'),
    path('GetPationsClinic', views.GetPatientsClinic.as_view(), name='GetPationsINClinic'),
    # path('/', views.ReservationsView.as_view(), name=''),
    # path('/', views.UploadMedicalRecord.as_view(), name=''),
]
