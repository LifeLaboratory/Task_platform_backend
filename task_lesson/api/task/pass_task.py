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
    def get_flag(data):
        """
        Метод получает флаг по таску и увенту
        :param data:
        :return:
        """
        try:
            task = TaskModel.objects.get(task=data[names.TASK], eventtask__task=data[names.TASK],
                                         eventtask__event=data[names.EVENT])
        except TaskModel.DoesNotExist:
            print("Task not found")
            return
        return task.flag

    @staticmethod
    def check_flag(db_flag, user_flag):
        """
        Сравнение флага из базы данных и присланного пользователем
        :param db_flag:
        :param user_flag:
        :return:
        """
        if db_flag is None:
            return False, 404
        if db_flag == user_flag:
            return True, 200
        else:
            return False, 400

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
        event_task = get_event_task(data[names.EVENT], data[names.TASK])
        team_user = get_team_user(data[names.USER], None)
        if event_task is not None and team_user is not None:
            event_task = SolutionModel(teamuser_id=team_user, eventtask_id=event_task, status=status, date=dt.now())
            event_task.save()

    def pass_task(self, responce):
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, names.PASS_TASK_FIELDS)
        set_types(data)
        db_flag = self.get_flag(data)
        checker, status = self.check_flag(db_flag, data[names.TASK_FLAG])
        self.insert_solution(data, checker)
        return HttpResponse(status=status)
