import json
from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Solution as SolutionModel
from task_lesson.api.helpers.checkers import set_types
from task_lesson.api.task.task import Task
from task_lesson.api.helpers.database import get_team_or_user
from task_lesson.api.helpers.database import get_event_task


class StatisticTask(Task):
    @staticmethod
    def solutions(data):
        """
        Метод по евенту и таску возвращает массивы с удачными сдачами флага и неудачными
        :param data:
        :return:
        """
        event_task = get_event_task(data[names.EVENT], data[names.TASK])
        if event_task:
            solved = SolutionModel.objects.filter(eventtask=event_task, status=True)
            unsolved = SolutionModel.objects.filter(eventtask=event_task, status=False)
            return solved, unsolved
        return None, None

    @staticmethod
    def post_proces_data(solved, unsolved):
        """
        Метод для постобработки данных из бд
        Возвращает словарь {
                            solved: количество удачных попыток сдачи флага
                            unsolved: количество неудачных попыток сдачи флага
                            solutions: массив словарей {
                                                        name: имя команды или пользователя сдавшего флаг
                                                        date: время сдачи
                                                       }
                            }
        :param solved:
        :param unsolved:
        :return:
        """
        solutions = []
        _dict = {}
        for solv in solved:
            data = get_team_or_user(solv.teamuser_id)
            if data:
                _dict['name'] = data.name
                _dict['date'] = solv.date.strftime("%H:%M:%S")
                solutions.append(_dict)

        _json = {
            'solved': len(solved),
            'unsolved': len(unsolved),
            'solutions': solutions
        }
        return _json

    def statistic_sends(self, responce):
        """
        Функция для получения статистики по конкретному таску
        собирает в себе вызовы всех методов, необходимые для получения статистики
        :param responce:
        :return:
        """
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, {names.TASK, names.EVENT})
        set_types(data)
        solved, unsolved = self.solutions(data)
        if solved or unsolved:
            answer = self.post_proces_data(solved, unsolved)
            return HttpResponse(json.dumps(answer))
        return HttpResponse(status=400)
