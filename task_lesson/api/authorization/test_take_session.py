


import json
import unittest as ut
# import api.authorization.get_session as gt
import api.helpers.names as names
import requests

from django.test import TestCase


class TestTakeSession(ut.TestCase):
    #  Пока не работает
    def setUp(self):

        self.user_id = 1

    def test_take_session(self):

        data = {
            'login': 'roman',
            'password': 'roman123'
        }
        # js_d = json.dumps(data)
        r = requests.post('http://127.0.0.1:8000/auth/', data=data)

        # _uuid = gt.Authorization.take_session(self.user_id)
        # self.assertIsInstance(_uuid, str, 'Некорректный тип сессии')
        return

    def test_auth(self):
        data = {
            'login': 'test_andrew',
            'password': 'test_andrew'
        }
        r = requests.post('http://127.0.0.1:8000/auth/', data=data)


        return
