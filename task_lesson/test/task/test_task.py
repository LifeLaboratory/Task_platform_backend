import unittest
import requests
import json
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
        responce = json.loads(r.text)
        pass

    def test_view_task(self):
        data = {
            names.EVENT: 1
        }
        r = requests.post('http://127.0.0.1:8000/api/task/view/', json=data)
        responce = json.loads(r.text)
        pass

    def test_pass_task(self):
        data = {
            names.EVENT: 1,
            names.TASK: 27,
            names.TASK_FLAG: 'CTF{test}',
            names.USER: 1
        }
        r = requests.post('http://127.0.0.1:8000/api/task/pass/', json=data)
        responce = json.loads(r.text)
        pass

    def test_edit_task(self):
        data = {
            'name': 'test_task_edit',
            'category': 'test',
            'weight': 10,
            'flag': 'CTF{test}',
            'description': 'test',
            names.USER: 1,
            names.EVENT: 1,
            names.TASK: 7
        }
        r = requests.post('http://127.0.0.1:8000/api/task/edit/', json=data)
        pass

    def test_solutions_task(self):
        data = {
            names.TASK: 27,
            names.EVENT: 1,

        }
        r = requests.post('http://127.0.0.1:8000/api/task/statistic_task/', json=data)
        pass