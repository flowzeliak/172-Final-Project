from django.test import TestCase
from .models import ExerType, Exerlog
from django.urls import reverse

# Create your tests here.
class ExerTypeTest(TestCase):
    def test_stringOutput(self):
        exertype=ExerType(exername='Urban Hiking')
        self.assertEqual(str(exertype), exertype.exername)

    def test_tablename(self):
        self.assertEqual(str(ExerType._meta.db_table), 'exertype')

#testing a view
class Testindex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'fitapp/index.html')