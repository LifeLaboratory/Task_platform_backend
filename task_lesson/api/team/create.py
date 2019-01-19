import task_lesson.api.helpers.names as names
import task_lesson.api.team.parent as pr
import json
from django.http import HttpResponse
from task_lesson.models import Team


class CreateTeam(pr.Team):
    def create(self, data):
        """
        Метод создет
        :param data:
        :return:
        """
        try:
            super(CreateTeam, self).create(data)
        except Exception as e:
            return HttpResponse(json.dumps({names.answer: e.args[1]}), 400)
        self._save()
        return self._make_response()

    def _save(self):
        """
        Метод сохраняет данные в базу
        :return:
        """
        self.save_object = Team(**self.data)
        self.save_object.save()

    def _make_response(self):
        self.data[names.TEAM_ID] = self.save_object.team
        response = self.data
        code = 200
        return HttpResponse(json.dumps(response), code)

    def __getattr__(self, item):
        value = None
        try:
            value = self.save_object.item
        except:
            value = None
        return value
