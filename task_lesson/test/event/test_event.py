import unittest
import requests
from task_lesson.api.helpers import names


class TestEvent(unittest.TestCase):
    def test_create_event(self):
        data = {
            names.EVENT_NAME: 'FirstEvent',
            names.EVENT_DESC: 'Main event',
            names.EVENT_PICTURE_URL: 'http://123.ru'
        }
        r = requests.post('http://127.0.0.1:8005/event/create/', data=data)
        pass
