
import json
import task_lesson.api.helpers.names as names
from task_lesson.models import TeamUser, Role, Event, EventTeamUser
from django.http import HttpResponse


class EventRegistrationTeam:

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        return names.AllGood

    @classmethod
    def set_eventteamuser(cls, request):

        data = json.loads(request.body.decode('utf-8'))
        answer = names.AllGood

        try:
            kwargs = {
                'event': Event.objects.get(pk=data['event']),
                'teamuser': TeamUser.objects.get(pk=data['teamuser']),
                'role': Role.objects.get(pk=data['role'])
            }
            evteus = EventTeamUser(**kwargs)
            evteus.save()

        except Exception as e:
            answer = names.ServerError

        return answer

    @classmethod
    def registation(cls, request):

        answer = cls.check_request(request)

        if answer == names.AllGood:
            answer = cls.set_eventteamuser(request)

        response = {
            names.ANSWER: answer
        }

        return HttpResponse(json.dumps(response))
