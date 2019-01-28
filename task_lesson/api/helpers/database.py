from task_lesson.models import EventSponsor
from task_lesson.models import TeamUser
from task_lesson.models import EventTask
from task_lesson.models import EventTeamUser
from task_lesson.models import Event


def get_team_user(user, no_team):
    """
    Функция возвращает teamuser
    no_team = True получить личный teamuser пользователя
    no_team = False получить список teamuser в которых пользователь - участник команды
    :param user: integer
    :param no_team: bool
    :return:
    """
    try:
        team_user = TeamUser.objects.filter(user=user, team__isnull=no_team)
        return team_user
    except TeamUser.DoesNotExist:
        print("TeamUser not found")
        return None


def get_team_user_in_event(user, event):
    """
    Функция возвращает teamuser по user в event
    :param user: integer
    :param event: integer
    :return:
    """

    try:
        team_user = TeamUser.objects.get(user_id=user, eventteamuser__event=event).teamuser
        return team_user
    except TeamUser.DoesNotExist:
        print("TeamUser not found")
        return None


def get_event_task(event, task):
    """
    Функция возвращает event_task по event и task
    :param event:
    :param task:
    :return:
    """
    try:
        event_task = EventTask.objects.get(event=event, task=task).eventtask
        return event_task
    except EventTask.DoesNotExist:
        print("EventTask not found")
        return None


def get_event_team_user(event, team_user):
    """
    Функция возвращает event_team_user по event и team_user
    :param event:
    :param team_user:
    :return:
    """
    try:
        event_team_user = EventTeamUser.objects.get(event=event, teamuser=team_user).eventteamuser
        return event_team_user
    except EventTeamUser.DoesNotExist:
        print("EventTeamUser not found")
        return None


def get_event_sponsor(event, sponsor):
    """
    Функция возвращает event_team_sponsor по event и sponsor
    :param event:
    :param sponsor:
    :return:
    """
    try:
        event_sponsor = EventSponsor.objects.get(event=event, sponsor=sponsor).eventsponsor
        return event_sponsor
    except EventSponsor.DoesNotExist:
        print("EventTeamUser not found")
        return None


def get_status_event(event):
    """
    Функция возвращает status события
    true - командное
    false - личное
    :param event:
    :return:
    """
    try:
        status = Event.objects.get(event=event).status
        return status
    except Event.DoesNotExist:
        print("EventTeamUser not found")
        return None
