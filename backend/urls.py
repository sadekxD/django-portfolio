from django.contrib import admin
from django.urls import path
from core.views import ProjectView, ContactView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/project-list/", ProjectView.as_view(), name="project-list"),
    path("api/contact/", ContactView.as_view(), name="contact"),
]
