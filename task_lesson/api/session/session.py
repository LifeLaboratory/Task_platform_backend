
import json
import task_lesson.api.helpers.names as names
from task_lesson.models import TeamUser, Role, Event, EventTeamUser
from django.http import HttpResponse
from django.core.cache import cache

class Session:

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        return names.AllGood

    @classmethod
    def get_user_id(cls, request):

        data = json.loads(request.body.decode('utf-8'))
        answer = names.AllGood
        user_id = None
        _uuid = data['session']
        try:
            user_id = cache.get(_uuid)
        except Exception as e:
            answer = names.ServerError

        return answer, user_id

    @classmethod
    def get_user_id_by_session(cls, request):

        answer = cls.check_request(request)

        if answer == names.AllGood:
            answer, user_id = cls.get_user_id(request)

        response = {
            names.ANSWER: answer,
            names.USER: user_id
        }

        return HttpResponse(json.dumps(response))
