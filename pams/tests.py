from django.test import TestCase
from .models import Patient

def create_dummy_patients():
    if Patient.objects.count() < 5:
        Patient.objects.bulk_create([
            Patient(full_name='John Doe', age=30, gender='M', insurance_provider='Aetna', policy_number='A12345'),
            Patient(full_name='Jane Smith', age=25, gender='F', insurance_provider='Cigna', policy_number='C67890'),
            Patient(full_name='Alex Johnson', age=40, gender='O', insurance_provider='UnitedHealth', policy_number='U11223'),
            Patient(full_name='Emily Davis', age=35, gender='F', insurance_provider='BlueCross', policy_number='B44556'),
            Patient(full_name='Michael Brown', age=50, gender='M', insurance_provider='Humana', policy_number='H77889'),
        ])

# Create your tests here.
