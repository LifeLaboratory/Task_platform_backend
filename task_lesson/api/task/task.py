from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Task as TaskModel
from task_lesson.models import EventTask as EventTaskModel
from task_lesson.api.helpers.checkers import set_types
import json


class Task:
    """
    Родительский класс для тасков
    """
    def __init__(self):
        self.row_data = None

    @staticmethod
    def parse_data(responce, fields):
        """
        Метод проверяет в запросе наличие необходимых полей и возвращает словарь с данными
        :param responce:
        :return: dict
        """
        data = dict()
        for k in fields:
            field = responce.POST.get(k, None)
            if field is not None:
                data[k] = field
        return data


class AddTask(Task):
    """
    Класс для добавления тасков в систему
    """
    @staticmethod
    def insert_task(data):
        """
        Метод производит запись таска в бд
        :param data:
        :return:
        """
        task = TaskModel(**data)
        task.save()
        return task.task

    @staticmethod
    def insert_event_task(data, task):
        """
        Метод производит запись связи события-таска
        :param data:
        :return:
        """
        event_task = EventTaskModel(event_id=data[names.EVENT], task_id=task)
        event_task.save()
        if event_task.eventtask is not None:
            return {names.ANSWER: names.OK, names.SESSION: ''}
        return {names.ANSWER: names.ERROR_REQUEST_DATABASE, names.SESSION: ''}

    def add_task(self, responce):
        """
        Разводящий метод для добавления тасков
        :param responce:
        :return:
        """
        self.row_data = responce
        data = self.parse_data(self.row_data, names.ADD_TASK_FIELDS)
        set_types(data)
        task = self.insert_task(data)
        if task:
            data = self.parse_data(self.row_data, names.EVENT_TASK_FIELDS)
            set_types(data)
            answer = self.insert_event_task(data, task)
            return HttpResponse(json.dumps(answer))
        return HttpResponse(json.dumps({names.ANSWER: names.ERROR_ADD_TASK, names.SESSION: ''}))

