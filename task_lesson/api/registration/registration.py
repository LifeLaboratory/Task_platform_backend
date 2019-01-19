
import json
import task_lesson.api.helpers.names as names
from task_lesson.models import User, TeamUser
from django.http import HttpResponse


class Registration:

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        # return names.RequestValueErorr
        return names.AllGood

    @classmethod
    def set_user(cls, request):

        data = json.loads(request.body.decode('utf-8'))
        answer = None
        # data = request.POST
        kwargs = {
            'name': data['name'],
            'login': data['login'],
            'password': data['password'],
            'email': data['email'],
        }
        try:
            user = User(**kwargs)
            user.save()
            team_user = TeamUser(**{'user': user})
            team_user.save()
        except Exception as e:
            answer = names.ServerError

        return answer

    @classmethod
    def registation(cls, request):

        answer = cls.check_request(request)

        if not answer:
            answer = cls.set_user(request)

        response = {
            names.ANSWER: answer
        }

        return HttpResponse(json.dumps(response))





