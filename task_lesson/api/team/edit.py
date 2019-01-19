import task_lesson.api.helpers.names as names
import task_lesson.api.team.parent as pr
import json
from django.http import HttpResponse


class EditTeam(pr.Team):
    def edit(self, data):
        """
        Метод для редактирования команды
        :param data:
        :return:
        """
        try:
            super(EditTeam, self).edit(data)
        except Exception as e:
            return HttpResponse(json.dumps({names.answer: e.args[1]}), 400)
        self._save()
        return self._make_response()

    def _make_response(self):
        """
        Метод формирует ответ сервера
        :return:
        """
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
