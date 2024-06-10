from django.urls import path
from . import views
from rest_framework import permissions

app_name = 'nurses'

urlpatterns = [
    path('profile/', views.GetProfile.as_view(), name='profile'),
    path('Casses/', views.GetPatientsClinic.as_view(), name='Casses'),
    path('Casses/Details/<int:id>', views.UserDetails.as_view(), name='UserDetails'),
    path('Rooms/<int:room_id>', views.GetCurrentRoom.as_view(), name='Room'),
    # path('Bed/', views.GetBed.as_view(), name='Bed'),
    path('Rooms/GetAll/', views.GetAllRooms.as_view(), name='AllRooms'),
    path('Rooms/History/', views.GetRoomsHistory.as_view(), name='RoomsHistory'),
    path('Room/Booked/', views.GetBookedRoom.as_view(), name='BookedRoom'),
    path('Room/Update/<int:bed_id>', views.UpdateRoom.as_view(), name='UpdateRoom'),
    path('Room/Add/<int:bed_id>', views.AddRoom.as_view(), name='AddRoom'),
    path('Calls/Current/', views.GetCurrentCalls.as_view(), name='CurrentCalls'),
    path('Calls/<int:Call_id>', views.GetCalls.as_view(), name='Calls'),
    path('Calls/GetAll/', views.GetAllCalls.as_view(), name='AllCalls'),
    path('Calls/Create/', views.CreateCalls.as_view(), name='CreateCalls'),
    path('Calls/Update/<int:Call_id>', views.UpdateCall.as_view(), name='UpdateCall'),
    
    # path('Casses/Details/<int:id>', views.UserDetails.as_view(), name='UserDetails'),
    # path('Calls/Update/<int:Call_id>', views.UpdateCall.as_view(), name='UpdateCall'),
    # path('Calls/Update/<int:Call_id>', views.UpdateCall.as_view(), name='UpdateCall'),
]
