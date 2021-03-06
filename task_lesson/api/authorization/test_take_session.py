


import json
import unittest as ut
# import api.authorization.authorization as gt
import api.helpers.names as names
import requests
import random

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
        r = requests.post('http://127.0.0.1:8000/api/auth/', data=data)

        # _uuid = gt.Authorization.set_session(self.user_id)
        # self.assertIsInstance(_uuid, str, 'Некорректный тип сессии')
        return

    def test_auth(self):
        data = {
            'login': 'test_andrew',
            'password': 'test_andrew'
        }
        r = requests.post('http://127.0.0.1:8000/api/auth/', data=json.dumps(data))


        return

    def test_registration(self):
        data = {
            'name': 'koderast' + str(random.random()),
            'login': 'sibir' + str(random.random()),
            'password': 'kotiki',
            'email': 'silence@gold.com',
        }
        r = requests.post('http://127.0.0.1:8000/api/registration/user/', data=json.dumps(data))


        return

    def test_registration_on_event(self):
        data = {
            'event': 1,
            'teamuser': 8,
            'role': 1
        }
        r = requests.post('http://127.0.0.1:8000/api/event/registration/team/', data=json.dumps(data))


        return

    def test_user_id_by_session(self):
        data = {
            'session': 'f8f056b4-44d8-47db-b383-8b4b56667a76'
        }
        r = requests.post('http://127.0.0.1:8000/api/get_user_id_by_session/', data=json.dumps(data))


        return