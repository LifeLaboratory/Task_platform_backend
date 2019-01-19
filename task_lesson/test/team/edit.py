import unittest
import requests
import json


class TestCreateTeam(unittest.TestCase):

    def test_create(self):
        test_data = {
            'team': 1,
            'name': 'test88',
            'pictureurl': 'http'
        }

        data = requests.post('http://127.0.0.1:8000/api/team/edit/', data=test_data)
        print(data.text)
        self.assertIsNone(json.loads(data.text).get('answer'))
