import unittest
import requests
from task_lesson.api.helpers import names


class TestTask(unittest.TestCase):
    def test_add_task(self):
        data = {
            'name': 'test_task',
            'category': 'test',
            'weight': 10,
            'flag': 'CTF{test}',
            'description': 'test',
            names.USER: 1,
            names.EVENT: 1
        }
        r = requests.post('http://127.0.0.1:8000/api/task/create/', json=data)
        pass

    def test_view_task(self):
        data = {
            names.EVENT: 1
        }
        r = requests.post('http://127.0.0.1:8000/api/task/view/', json=data)
        pass
