import task_lesson.api.helpers.names as names
import task_lesson.models as model
from task_lesson.api.helpers.checkers import check_dict


class Team:
    def __init__(self):
        self.data = {}
        self.response = None
        self.session = None

    def _get_session(self):
        self.id_user = 1
        self.data[names.TEAM_USER_ID] = self.id_user

    def check_team(self):
        if model.Team.objects.filter(name=self.data[names.TEAM_NAME]).last():
            raise Exception(names.answer, names.NameTeamIsNotEmpty)

    def create(self, response):
        self.data, self.response = check_dict(response.POST, names.ADD_TEAM_FIELDS)
        self._get_session()
        self.check_team()
