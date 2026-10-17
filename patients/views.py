

from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    RegisterSerializer,
    PatientSerializer,
    DoctorSerializer,
    PatientDoctorMappingSerializer,
)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.filter(
            patient__created_by=request.user
        )
        return Response(
            PatientDoctorMappingSerializer(mappings, many=True).data
        )

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        patient = serializer.validated_data['patient']
        if patient.created_by != request.user:
            raise PermissionDenied(
                "You can only assign doctors to your own patients."
            )

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientMappingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        patient = get_object_or_404(
            Patient, pk=patient_id, created_by=request.user
        )
        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        return Response(
            PatientDoctorMappingSerializer(mappings, many=True).data
        )

    def delete(self, request, patient_id):
        mapping = get_object_or_404(
            PatientDoctorMapping,
            pk=patient_id,
            patient__created_by=request.user
        )
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
