from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.print_hello),
    path('details/', views.details),
    path ('add/', views.add),
    path ('edit/<pk>', views.edit),
    path ('delete/<pk>', views.delete)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)