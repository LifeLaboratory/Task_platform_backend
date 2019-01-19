
from task_lesson.models import User
from django.http import HttpResponse


class Registration:

    @classmethod
    def check_request(cls, request):
        """Проверка входных данных на корректность"""
        # return names.RequestValueErorr
        return None

    @classmethod
    def set_user(cls, request):

        answer = None
        data = request.POST
        kwargs = {
            'name': data['name'],
            'login': data['login'],
            'password': data['password'],
            'email': data['email'],
        }
        try:
            user = User(**kwargs)
            user.save()
        except Exception as e:
            answer = e

        return answer

    @classmethod
    def registation(cls, request):

        answer = cls.check_request(request)

        if not answer:
            answer = cls.set_user(request)

        response = {
            'content': answer if answer else None,
            'status': 500 if answer else 200,
            'reason': answer if answer else 200
        }

        return HttpResponse(**response)





