from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestFib(TestCase):
  def test_valid_input(self):
    response = self.client.get(reverse('fib_api'), {'n': 99})
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), {'result': 218922995834555169026})
  
  def test_invalid_input(self):
    response = self.client.get(reverse('fib_api'), {'n': -1})
    self.assertEqual(response.status_code, 400)
    self.assertEqual(response.json(), {"status": 400, "message": 'Invalid input. Please provide a positive integer.'})
  
  def test_invalid_input2(self):
    response = self.client.get(reverse('fib_api'), {'n': 'aaaa'})
    self.assertEqual(response.status_code, 400)
    self.assertEqual(response.json(), {"status": 400, "message": 'Invalid input. Please provide a valid positive integer.'})