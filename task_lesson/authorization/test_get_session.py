

import unittest as ut
import json
import task_lesson.authorization.get_session as gt

class TestGetSession(ut.TestCase):

    class Dymmy:
        pass

    def setUp(self):

        self.response = {
            'answer': None,
            'session': None,
            'user_id': None
        }

    def fix_good_check(self, request):
        return None

    def fix_error_check(self, request):
        return gt.Authorization.RequestValueErorr

    def fix_have_not_login(self, request):
        self.response['answer'] = gt.Authorization.LoginError
        return self.response

    def fix_have_not_password(self, request):
        self.response['answer'] = gt.Authorization.PasswordError
        return self.response

    def fix_have_id_user(self, request):
        self.response['user_id'] = 1
        return self.response

    def fix_have_not_take_session(self, user_id):
        return None

    def test_error_login(self):

        request = ''
        answer = gt.Authorization.LoginError
        gt.Authorization.check_request = self.fix_good_check
        gt.Authorization.get_id_user = self.fix_have_not_login
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            'answer': answer,
            'session': None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')

    def test_error_password(self):

        answer = gt.Authorization.PasswordError
        request = ''
        gt.Authorization.check_request = self.fix_good_check
        gt.Authorization.get_id_user = self.fix_have_not_password
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            'answer': answer,
            'session': None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')

    def test_error_request(self):

        answer = gt.Authorization.RequestValueErorr
        request = ''
        gt.Authorization.check_request = self.fix_error_check
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            'answer': answer,
            'session': None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')

    def test_error_create_session(self):

        answer = gt.Authorization.CreateSessionError
        request = ''
        gt.Authorization.check_request = self.fix_good_check
        gt.Authorization.get_id_user = self.fix_have_id_user
        gt.Authorization.take_session = self.fix_have_not_take_session
        response = gt.Authorization.get_session(request)

        dict_r = json.loads(response)
        reference = {
            'answer': answer,
            'session': None
        }
        self.assertEqual(reference, dict_r, 'Неожиданный реультат')