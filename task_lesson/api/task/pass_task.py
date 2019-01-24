import json
from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Task as TaskModel
from task_lesson.models import Solution as SolutionModel
from task_lesson.api.helpers.checkers import set_types
from task_lesson.api.task.task import Task
from task_lesson.api.helpers.database import *
from datetime import datetime as dt


class PassTask(Task):
    @staticmethod
    def check_flag(data):
        """
        Метод сверяет присланный флаг с флагом из базы данных по заданному таску в событии
        :param data:
        :return:
        """
        try:
            task = TaskModel.objects.get(task=data[names.TASK], eventtask__task=data[names.TASK],
                                         flag=data[names.TASK_FLAG], eventtask__event=data[names.EVENT])
        except TaskModel.DoesNotExist:
            print("Task not found")
            return
        if task is not None:
            return True, 200
        else:
            return False, 400
        return task.task

    @staticmethod
    def insert_solution(data, status):
        """
        Производит запись в таблицу solution
        status = True - успешно сдан флаг
        status = False - неудачная попытка
        :param data:
        :param status:
        :return:
        """
        event = data.get(names.EVENT)
        user = data.get(names.USER)
        event_task = get_event_task(event, data[names.TASK])
        team_user = get_team_user_in_event(user, event)
        if event_task is not None and team_user is not None:
            event_task = SolutionModel(teamuser_id=team_user, eventtask_id=event_task, status=status, date=dt.now())
            event_task.save()

    def pass_task(self, responce):
        """
        Функция для сдачи флагов
        собирает в себе вызовы всех методов, необходимые для сдачи флага
        :param responce:
        :return:
        """
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, names.PASS_TASK_FIELDS)
        set_types(data)
        checker, status = self.check_flag(data)
        self.insert_solution(data, checker)
        return HttpResponse(status=status)
