from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("mentorship_api/", include("mentorship.urls")),
    path("testing_system_api/", include("testing_system.urls")),
    path("chat/", include("chat.urls")),
]
