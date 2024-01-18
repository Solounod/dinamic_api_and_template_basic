from django.test import TestCase
from .models import Services

class ServicesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Services.objects.create(name_service='Test Service', description_service='This is a test service')

    def test_name_service_label(self):
        service = Services.objects.get(id=1)
        field_label = service._meta.get_field('name_service').verbose_name
        self.assertEquals(field_label, 'Nombre')

    def test_description_service_label(self):
        service = Services.objects.get(id=1)
        field_label = service._meta.get_field('description_service').verbose_name
        self.assertEquals(field_label, 'Descripción')

    def test_name_service_max_length(self):
        service = Services.objects.get(id=1)
        max_length = service._meta.get_field('name_service').max_length
        self.assertEquals(max_length, 100)