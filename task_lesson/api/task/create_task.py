from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Task as TaskModel
from task_lesson.api.helpers.checkers import set_types
from task_lesson.api.task.task import Task
import json
from task_lesson.models import EventTask as EventTaskModel


class CreateTask(Task):
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
        task = TaskModel(
            name=data[names.TASK_NAME],
            category=data[names.TASK_CATEGORY],
            weight=data[names.TASK_WEIGHT],
            flag=data[names.TASK_FLAG],
            description=data[names.TASK_DESCRIPTION],
            user_id=data[names.USER]
        )
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

    def create_task(self, responce):
        """
        Разводящий метод для добавления тасков
        :param responce:
        :return:
        """
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, names.CREATE_TASK_FIELDS)
        set_types(data)
        task = self.insert_task(data)
        if task:
            answer = self.insert_event_task(data, task)
            return HttpResponse(json.dumps(answer))
        return HttpResponse({names.ANSWER: names.ERROR_ADD_TASK, names.SESSION: ''})
