import unittest
import requests
import json


class TestCreateTeam(unittest.TestCase):

    def test_create(self):
        test_data = {
            'team': 1,
            'name': 'test86',
            'pictureurl': 'http'
        }

        data = requests.post('http://90.189.132.25:7777/team/edit/', data=test_data)
        print(data.text)
        self.assertIsNone(json.loads(data.text).get('answer'))
