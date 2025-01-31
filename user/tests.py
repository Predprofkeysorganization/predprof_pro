from django.test import TestCase
import requests

"""Демонстрация и тестирование поддержки интеграции с внешними системами для автоматизации
закупок. Взаимодействие с внешними системами происходит через API"""


def demonstration():
    print(requests.get('http://127.0.0.1:8000/api/apikey/').json())


demonstration()
