from django.urls import path,include
from .views import RegisterUser,ClientViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin

#register the clientView using rest frameworks router
router = DefaultRouter()
router.register(r'Client', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #to register new users
    path('register/', RegisterUser.as_view(), name='register'),
    #the api for the clientviewset
    path('client', include(router.urls))
]
