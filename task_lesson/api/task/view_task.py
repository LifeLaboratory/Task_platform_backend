from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Task as TaskModel
from task_lesson.api.helpers.checkers import set_types
from task_lesson.api.task.task import Task
import json


class ViewTask(Task):
    @staticmethod
    def get_tasks(filter):
        """
        Метод получает таски по заданному фильтру
        :param data:
        :return:
        """
        if filter.get(names.TASK_CATEGORY, None):
            tasks = TaskModel.objects.filter(category=filter[names.TASK_CATEGORY], eventtask__event=filter[names.EVENT])
        else:
            tasks = TaskModel.objects.filter(eventtask__event=filter[names.EVENT])
        return tasks

    @staticmethod
    def make_responce(tasks):
        data = []
        for t in tasks:
            _dict = dict()
            for key in names.TASK_FIELDS:
                _dict[key] = t.__getattribute__(key)
            data.append(_dict)
        return {names.ANSWER: data}

    def view_task(self, responce):
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, names.VIEW_TASK_FIELDS)
        set_types(data)
        tasks = self.get_tasks(data)
        answer = self.make_responce(tasks)
        return HttpResponse(json.dumps(answer))
