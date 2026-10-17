



from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        read_only_fields = ['id']

    def validate_email(self, value):
        email = value.strip().lower()

        if User.objects.filter(username__iexact=email).exists():
            raise serializers.ValidationError(
                "This email is already registered. Please log in."
            )

        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                "This email is already registered. Please log in."
            )

        return email

    def create(self, validated_data):
        name = validated_data.pop('name')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        return User.objects.create_user(
            username=email,
            first_name=name,
            email=email,
            password=password
        )


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ['assigned_at']
