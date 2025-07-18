from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clinicaApp.views import PacienteViewSet, HistoriaClinicaViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API de Historias Clínicas",
        default_version='v1',
        description="Documentación de la API REST de tu proyecto en Django",
        terms_of_service="https://www.ejemplo.com/terminos/",
        contact=openapi.Contact(email="moises.perez@ejemplo.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias', HistoriaClinicaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
