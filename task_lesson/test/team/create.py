import unittest
import requests
import json


class TestCreateTeam(unittest.TestCase):

    def test_create(self):
        test_data = {
            'name': 'test7',
            'pictureurl': 'http'
        }

        data = requests.post('http://127.0.0.1:8000/team/', data=test_data)

        self.assertIsNone(json.loads(data.text).get('answer'))
