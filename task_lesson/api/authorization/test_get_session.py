

import unittest as ut
import json
import api.authorization.get_session as gt
import api.helpers.names as names

class TestGetSession(ut.TestCase):

    def setUp(self):

        self.response = {
            names.ANSWER: None,
            names.SESSION: None,
            names.USER: None
        }

    def fix_good_check(self, request):
        return None

    def fix_error_check(self, request):
        return names.RequestValueErorr

    def fix_have_not_login(self, request):
        self.response[names.ANSWER] = names.LoginError
        return self.response

    def fix_have_not_password(self, request):
        self.response[names.ANSWER] = names.PasswordError
        return self.response

    def fix_have_id_user(self, request):
        self.response[names.USER] = 1
        return self.response

    def fix_have_not_take_session(self, user_id):
        return None

    def test_error_login(self):

        request = ''
        answer = names.LoginError
        gt.Authorization.check_request = self.fix_good_check
        gt.Authorization.get_id_user = self.fix_have_not_login
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            names.ANSWER: answer,
            names.SESSION: None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')

    def test_error_password(self):

        answer = names.PasswordError
        request = ''
        gt.Authorization.check_request = self.fix_good_check
        gt.Authorization.get_id_user = self.fix_have_not_password
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            names.ANSWER: answer,
            names.SESSION: None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')

    def test_error_request(self):

        answer = names.RequestValueErorr
        request = ''
        gt.Authorization.check_request = self.fix_error_check
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            names.ANSWER: answer,
            names.SESSION: None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')

    def test_error_create_session(self):

        answer = names.CreateSessionError
        request = ''
        gt.Authorization.check_request = self.fix_good_check
        gt.Authorization.get_id_user = self.fix_have_id_user
        gt.Authorization.take_session = self.fix_have_not_take_session
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            names.ANSWER: answer,
            names.SESSION: None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')