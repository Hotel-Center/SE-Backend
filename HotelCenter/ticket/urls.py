from django.urls import path
from .views import TypeRequestsList,MyTicketList,ResponseAdminAPIs





urlpatterns = [
                        path('new_type_request/',TypeRequestsList.as_view()),
                        path('myticket/',MyTicketList.as_view()),
                        path('response_admin/<int:pk>',ResponseAdminAPIs.as_view())
]
