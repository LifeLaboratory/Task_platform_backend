from django.db import models

# Create your models here.


class User(models.Model):
    user = models.IntegerField(primary_key=True)
    name = models.CharField()
    login = models.CharField()
    password = models.CharField()
    email = models.CharField()

    def __str__(self):
        return self.user


class Role(models.Model):
    role = models.IntegerField(primary_key=True)
    name = models.CharField()


class Team(models.Model):
    team = models.IntegerField(primary_key=True)
    name = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pictureurl = models.CharField()


class TeamUser(models.Model):
    teamuser = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.BooleanField(default=None)


class Event(models.Model):
    event = models.IntegerField(primary_key=True)
    name = models.CharField()
    pictureurl = models.CharField()
    description = models.CharField()


class EventTeamUser(models.Model):
    eventteamuser = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    teamuser = models.ForeignKey(TeamUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Task(models.Model):
    task = models.IntegerField(primary_key=True)
    name = models.CharField()
    category = models.CharField()
    weight = models.FloatField()
    flag = models.CharField()
    description = models.CharField()
    # Автор задания
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class EventTask(models.Model):
    eventtask = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class Sponsor(models.Model):
    sponsor = models.IntegerField(primary_key=True)
    name = models.CharField()
    pictureurl = models.CharField()


class EventSponsor(models.Model):
    eventsponsor = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)


class Hint(models.Model):
    hint = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Solution(models.Model):
    solution = models.IntegerField(primary_key=True)
    teamuser = models.ForeignKey(TeamUser, on_delete=models.CASCADE)
    eventtask = models.ForeignKey(EventTask, on_delete=models.CASCADE)
