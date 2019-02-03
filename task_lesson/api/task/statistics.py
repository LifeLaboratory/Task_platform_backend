import json
from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Solution as SolutionModel
from task_lesson.api.helpers.checkers import set_types
from task_lesson.api.task.task import Task
from task_lesson.api.helpers.database import *


class StatisticTask(Task):
    @staticmethod
    def solved_solutions(data):
        event_task = get_event_task(data[names.EVENT], data[names.TASK])
        solutions = SolutionModel.objects.filter(eventtask=event_task, status=True)
        return solutions

    @staticmethod
    def unsolved_solutions(data):
        event_task = get_event_task(data[names.EVENT], data[names.TASK])
        solutions = SolutionModel.objects.filter(eventtask=event_task, status=False)
        return solutions

    def statistic_sends(self, responce):
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, {names.TASK, names.EVENT})
        set_types(data)
        solved = self.solved_solutions(data)
        unsolved = self.unsolved_solutions(data)

        return HttpResponse(json.dumps(
            {
                'solved': len(solved),
                'unsolved': len(unsolved)
            }
        ))
