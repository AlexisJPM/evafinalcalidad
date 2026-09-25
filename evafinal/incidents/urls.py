from django.urls import path
from .views import *

urlpatterns = [
    path("", incident_list, name="incident_list"),
    path("incidents/<int:id>", incident_detail, name="incident_detail"),
    path("incidents/create", incident_create, name="incident_create"),
    path("incidents/update/<int:id>", incident_update, name="incident_update"),
    path("incidents/delete/<int:id>", incident_delete, name="incident_delete"),
]