from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import ProjectView, ContactView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/project-list/", ProjectView.as_view(), name="project-list"),
    path("api/contact/", ContactView.as_view(), name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
