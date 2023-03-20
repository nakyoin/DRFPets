from . import views
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()

router.register(r'shop', views.PetApiView)

urlpatterns = [
     path('', views.PetApiView.as_view()),
     path('<int:pk>/', views.SinglePetView.as_view()),
     path('cart/', views.OrderApiView.as_view()),
     path('cart/<int:pk>', views.OrderView.as_view()),

]