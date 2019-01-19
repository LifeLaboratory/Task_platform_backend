

import unittest as ut
import json
import api.authorization.get_session as gt
import api.helpers.names as names

class TestTakeSession(ut.TestCase):
    #  Пока не работает
    def setUp(self):

        self.user_id = 1

    def test_take_session(self):

        _uuid = gt.Authorization.take_session(self.user_id)
        self.assertIsInstance(_uuid, str, 'Некорректный тип сессии')