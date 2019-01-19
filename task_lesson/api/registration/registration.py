
from task_lesson.models import User


class Registration:

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        # return names.RequestValueErorr
        return None

    @classmethod
    def set_user(cls, request):

        data = request.POST
        user = User()

    @classmethod
    def registation(cls, request):

        answer = cls.check_request(request)

        if not answer:
            pass





