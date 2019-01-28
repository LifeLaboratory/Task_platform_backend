import json
from django.http import HttpResponse
from task_lesson.api.helpers import names
from task_lesson.models import Task as TaskModel
from task_lesson.api.helpers.checkers import set_types
from task_lesson.api.task.task import Task


class EditTask(Task):
    @staticmethod
    def update_task(data):
        """
        Метод производит запись таска в бд
        :param data:
        :return:
        """
        try:
            task = TaskModel.objects.get(task=data[names.TASK])
        except TaskModel.DoesNotExist:
            print("Task not found")
            return
        task.name = data.get(names.TASK_NAME)
        task.category = data.get(names.TASK_CATEGORY)
        task.weight = data.get(names.TASK_WEIGHT)
        task.flag = data.get(names.TASK_FLAG)
        task.description = data.get(names.TASK_DESCRIPTION)
        task.user_id = data.get(names.USER)
        task.save()
        return 200

    def edit_task(self, responce):
        """
        Метод редактирует таск
        :param responce:
        :return:
        """
        self.row_data = json.loads(responce.body.decode('utf-8'))
        data = self.parse_data(self.row_data, names.CREATE_TASK_FIELDS)
        set_types(data)
        status = self.update_task(data)
        return HttpResponse(status=status)
