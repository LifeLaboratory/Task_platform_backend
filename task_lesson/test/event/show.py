import unittest
import requests
import json


class TestShowTeam(unittest.TestCase):

    def test_show(self):
        data = requests.get('http://127.0.0.1/event/list/')
        print(data.text)
        # self.assertIsNone(json.loads(data.text).get('answer'))
