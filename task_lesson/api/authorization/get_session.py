

__author__= 'rv.fomichev'

import json
import redis
import django_redis
import api.helpers.names as names

from django.core.cache import cache
from uuid import uuid4


class Authorization:

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        return cls.RequestValueErorr

    @classmethod
    def get_id_user(cls, request):

        return {
            names.ANSWER: cls.LoginError,
            names.USER: None
        }

    @classmethod
    def take_session(cls, user_id):
        """Установка сессии для юзера"""
        _uuid = str(uuid4())
        cache.set(_uuid, user_id, timeout=names.TimeOutSession)
        return _uuid

    @classmethod
    def get_session(cls, request):

        session = None
        answer = cls.check_request(request)
        if not answer:

            user_dict = cls.get_id_user(request)
            user_id = user_dict[names.USER]
            if user_id:
                session = cls.take_session(user_id)
                if not session:
                    answer = names.CreateSessionError
            else:
                answer = user_dict[names.ANSWER]

        response = {
            names.ANSWER: answer,
            names.SESSION: session
        }

        return json.dumps(response)