from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clinicaApp.views import PacienteViewSet, HistoriaClinicaViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias', HistoriaClinicaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # ← Aquí expones tu API
]
