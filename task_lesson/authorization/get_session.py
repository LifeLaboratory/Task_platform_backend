

__author__= 'rv.fomichev'

import json
import redis
import django_redis

from django.core.cache import cache
from uuid import uuid4

# str(uuid4())

class Authorization:


    CreateSessionError = 'Не удалось авторизоватся. Повторите попытку позже.'
    RequestValueErorr = 'Получен не корректный запрос на авторизацию'
    LoginError = 'Пользователя с таким логином не существует'
    PasswordError = 'Неверный пароль'

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        return cls.RequestValueErorr

    @classmethod
    def get_id_user(cls, request):

        return {
            'answer': cls.LoginError,
            'user_id': None
        }

    @classmethod
    def take_session(cls, user_id):

        return

    @classmethod
    def get_session(cls, request):

        session = None
        answer = cls.check_request(request)
        if not answer:

            user_dict = cls.get_id_user(request)
            user_id = user_dict['user_id']
            if user_id:
                session = cls.take_session(user_id)
                if not session:
                    answer = cls.CreateSessionError
            else:
                answer = user_dict['answer']

        response = {
            'answer': answer,
            'session': session
        }

        return json.dumps(response)