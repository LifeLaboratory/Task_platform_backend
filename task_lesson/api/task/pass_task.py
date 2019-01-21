from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Task as TaskModel
from task_lesson.models import Solution as SolutionModel
from task_lesson.api.helpers.checkers import set_types
from task_lesson.api.task.task import Task
import json
from task_lesson.models import EventTask as EventTaskModel
from datetime import datetime as dt
from task_lesson.api.helpers.database import get_teamuser


class PassTask(Task):
    @staticmethod
    def get_flag(data):
        """
        Метод получает таски по заданному фильтру
        :param data:
        :return:
        """
        tasks = TaskModel.objects.filter(task=data[names.TASK], eventtask__task=data[names.TASK],
                                      eventtask__event=data[names.EVENT]
                                         )
        return tasks.flag


    @staticmethod
    def check_flag(db_flag, user_flag):
        if db_flag == user_flag:
            status = True
        else:
            status = False

#        solution = SolutionModel(teamuser=, eventtask=, status=status, date=dt.now())
#        event_task.save()

    def pass_task(self, responce):
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, names.PASS_TASK_FIELDS)
        set_types(data)
        db_flag = self.get_flag(data)
        get_teamuser(data)
        # self.check_flag(db_flag, data[names.TASK_FLAG])

        return None # HttpResponse(json.dumps(answer))
