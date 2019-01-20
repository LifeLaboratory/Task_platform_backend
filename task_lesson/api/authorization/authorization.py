import json
import task_lesson.api.helpers.names as names

from django.core.cache import cache
from uuid import uuid4
from task_lesson.models import User
from django.http import HttpResponse

__author__ = 'rv.fomichev'


class Authorization:

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        return names.AllGood

    @classmethod
    def get_id_user(cls, request):

        data = json.loads(request.body.decode('utf-8'))
        qset = User.objects.filter(login=data['login'], password=data['password'])
        if len(qset):
            answer = None
            user_id = qset[0].user
        else:
            answer = names.AuthorizationError
            user_id = None
        return {
            names.ANSWER: answer,
            names.USER: user_id
        }

    @classmethod
    def set_session(cls, user_id):
        """Установка сессии для юзера"""
        _uuid = str(uuid4())
        cache.set(_uuid, user_id, timeout=names.TimeOutSession)
        return _uuid

    @classmethod
    def authorization(cls, request):

        session = None
        answer = cls.check_request(request)
        if answer == names.AllGood:

            user_dict = cls.get_id_user(request)
            user_id = user_dict[names.USER]
            if user_id:
                session = cls.set_session(user_id)
                if not session:
                    answer = names.ServerError
            else:
                answer = user_dict[names.ANSWER]

        response = {
            names.ANSWER: answer,
            names.SESSION: session
        }

        return HttpResponse(json.dumps(response))
