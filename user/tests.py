from django.test import TestCase
import requests

print(requests.post('http://127.0.0.1:8000/api/router/',
                    json={'id_application': '55', 'status_application': 'одобрена'}).json())