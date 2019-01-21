from task_lesson.models import EventSponsor
from task_lesson.models import TeamUser
from task_lesson.models import EventTask
from task_lesson.models import EventTeamUser


def get_team_user(user):
    """
    Функция получает teamuser по user и team
    :param user:
    :param team:
    :return:
    """
    try:
        team_user = TeamUser.objects.filter(user=user)
        return team_user
    except TeamUser.DoesNotExist:
        print("TeamUser not found")
        return None


def get_personal_team_user(user):
    """
    Функция получает teamuser с team = Null
    :param user:
    :param team:
    :return:
    """
    list_team_user = get_team_user(user)
    for tu in list_team_user:
        if tu.team is None:
            return tu.teamuser
    return None


def get_event_task(event, task):
    """
    Функция получает event_task по event и task
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
    Функция получает event_team_user по event и team_user
    :param event:
    :param team_user:
    :return:
    """
    try:
        event_team_user = EventTeamUser.objects.get(event=event, teamuser=team_user)
        return event_team_user
    except EventTeamUser.DoesNotExist:
        print("EventTeamUser not found")
        event_team_user = EventTeamUser
        event_team_user.eventteamuser = None
        return event_team_user


def get_event_sponsor(event, sponsor):
    """
    Функция получает event_team_sponsor по event и sponsor
    :param event:
    :param sponsor:
    :return:
    """
    try:
        event_sponsor = EventSponsor.objects.get(event=event, sponsor=sponsor)
        return event_sponsor
    except EventSponsor.DoesNotExist:
        print("EventTeamUser not found")
        event_sponsor = EventSponsor
        event_sponsor.eventsponsor = None
        return event_sponsor
