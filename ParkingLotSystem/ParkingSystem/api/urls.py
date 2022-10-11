from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('person-address/', views.personAddress, name="person-address"),
    path('address-detail/', views.addressDetail, name="address-detail"),
    path('post-cardetail/', views.postCarDetail, name="post-cardetail"),
    path('get-cardetail/', views.getCarDetail, name="get-cardetail"),
    path('car-exit/<str:pk>/', views.carExit, name="car-exit"),
    path('person-account/', views.personAccount, name="person-account"),
    path('get-accountdetail/', views.getAccountDetail, name="get-accountdetail"),
    path('person-accountupdate/<str:pk>/', views.personAccountUpdate, name="person-accountupdate"),

]
