from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from history.views import HistoryView

router = routers.DefaultRouter()

router.register("history", HistoryView, basename="history")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls))
]
