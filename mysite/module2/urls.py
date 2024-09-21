from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.print_hello),
    path('details/', views.details),
    path ('add/', views.add),
    path ('edit/<pk>', views.edit),
    path ('delete/<pk>', views.delete)

]