from task_lesson.api.event.generic import Event
import task_lesson.api.helpers as helpers
import task_lesson.api.helpers.names as names
import json
from task_lesson.models import Event, EventTeamUser
from django.http import HttpResponse
from django.db.models import Count


class ShowEvent:
    @staticmethod
    def get_list_event(response):
        all_event = [event.event for event in Event.objects.all()]
        return HttpResponse(json.loads({names.ANSWER: all_event}))
