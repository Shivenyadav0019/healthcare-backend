

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    PatientViewSet,
    DoctorViewSet,
    RegisterView,
    MappingListCreateView,
    PatientMappingDetailView,
)

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patient')
router.register('doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', PatientMappingDetailView.as_view(), name='mapping-detail'),
    path('', include(router.urls)),
]
