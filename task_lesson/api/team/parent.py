import task_lesson.api.helpers.names as names
import task_lesson.models as model
import json
from task_lesson.api.helpers.checkers import check_dict


class Team:
    def __init__(self):
        self.data = {}
        self.response = None
        self.session = None

    def _get_session(self):
        """
        Метод получения сессии
        :return:
        """
        self.id_user = 1
        self.data[names.TEAM_USER_ID] = self.id_user

    def _save(self):
        """
        Метод сохраняет данные в базу
        :return:
        """
        self.save_object = model.Team(**self.data)
        self.save_object.save()

    def check_team(self):
        """
        Метод проверяет, есть ли такое же имя команды
        :return:
        """
        team = self.data.get(names.TEAM_ID, None)
        if model.Team.objects.filter(name=self.data[names.TEAM_NAME]).last():
            if team:
                if model.Team.objects.filter(name=self.data[names.TEAM_NAME]).filter(team=team).last():
                    raise Exception(names.answer, names.NameTeamIsNotEmpty)
            else:
                raise Exception(names.answer, names.NameTeamIsNotEmpty)

    def check_param(self, response, check_param):
        """
        Метод проверяет входные данные по типу
        :param response:
        :param check_param:
        :return:
        """
        self.data, self.response = check_dict(json.loads(response.body.decode('utf-8')), check_param)

    def create(self, response):
        """
        Метод создания команды
        :param response:
        :return:
        """
        self.check_param(response, names.ADD_TEAM_FIELDS)
        self._get_session()
        self.check_team()

    def edit(self, response):
        """
        Метод для редактирования команды
        :param response:
        :return:
        """
        self.check_param(response, names.EDIT_TEAM_FIELDS)
        self._get_session()
        self.check_team()

    def __getattr__(self, item):
        value = None
        try:
            value = self.save_object.item
        except:
            value = None
        return value
