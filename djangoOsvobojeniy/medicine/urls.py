from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('info/<int:pk>', views.PacientInfoDetailView.as_view(), name="pacient-detail"),
    path('create', views.create, name="New-pacient"),
    path('info/<int:pk>/edit', views.update, name="pacient-update"),
    path('info/<int:pk>/delete', views.delete, name="pacient-delete"),
]

