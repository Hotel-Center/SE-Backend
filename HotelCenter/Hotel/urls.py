"""Hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from .api.hotel import HotelViewSet, FacilityViewSet
from .api.room import RoomList, roomFacilityViewSet, ImageList
from .api.hotel import HotelViewSet, FacilityViewSet, HotelImgViewSet, BestHotelViewSet
from .api.room import RoomList, roomFacilityViewSet, ImageList, RoomSpaceViewSet

router = routers.DefaultRouter()
router.register('hotels', HotelViewSet, basename='user-hotel')
router.register('facilities', FacilityViewSet, basename='facility-list')
router.register('best', BestHotelViewSet, basename='best-hotel')
hotel_router = routers.DefaultRouter()
hotel_router.register('images', HotelImgViewSet, basename='hotel-images')
router.register('roomfacilities', roomFacilityViewSet, basename='roomfacility-list')

urlpatterns = [
    path('room/<int:hotel_id>/', RoomList.as_view()),
    path('room/<int:room_id>/images/', ImageList.as_view()),
    path('', include(router.urls)),
    path('<int:hid>/', include(hotel_router.urls)),

]
