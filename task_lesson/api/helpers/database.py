from task_lesson.models import User
from task_lesson.models import TeamUser


def get_teamuser(user, event):
    teamuser = TeamUser.objects.filter(user=user)
    pass
