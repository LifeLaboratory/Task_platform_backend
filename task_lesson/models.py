from django.db import models

# Create your models here.


class User(models.Model):
    user = models.AutoField(primary_key=True)
    name = models.TextField(max_length=128, default='', null=False)
    login = models.TextField(max_length=128, default='', null=False)
    password = models.TextField(max_length=128, default='', null=False)
    email = models.TextField(max_length=128, default='', null=False)


class Role(models.Model):
    role = models.AutoField(primary_key=True)
    name = models.TextField(max_length=128, default='', null=False)


class Team(models.Model):
    team = models.AutoField(primary_key=True)
    name = models.TextField(max_length=128, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pictureurl = models.TextField(max_length=128, default='', null=False)


class TeamUser(models.Model):
    teamuser = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=False, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.BooleanField(default=None, null=True)


class Event(models.Model):
    event = models.AutoField(primary_key=True)
    name = models.TextField(max_length=128, default='', null=False)
    pictureurl = models.TextField(max_length=128, default='', null=False)
    description = models.TextField(max_length=10000, default='', null=False)


class EventTeamUser(models.Model):
    eventteamuser = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    teamuser = models.ForeignKey(TeamUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Task(models.Model):
    task = models.AutoField(primary_key=True)
    name = models.TextField(max_length=128, default='', null=False)
    category = models.TextField(max_length=128, default='', null=False)
    weight = models.FloatField(max_length=128, default=0.0, null=False)
    flag = models.TextField(max_length=128, default='', null=False)
    description = models.TextField(max_length=10000, default='', null=False)
    # Автор задания
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class EventTask(models.Model):
    eventtask = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class Sponsor(models.Model):
    sponsor = models.AutoField(primary_key=True)
    name = models.TextField(max_length=128, null=False)
    pictureurl = models.TextField(max_length=128, default='', null=False)


class EventSponsor(models.Model):
    eventsponsor = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)


class Hint(models.Model):
    hint = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField(max_length=2048, default='', null=False)


class Solution(models.Model):
    solution = models.AutoField(primary_key=True)
    teamuser = models.ForeignKey(TeamUser, on_delete=models.CASCADE)
    eventtask = models.ForeignKey(EventTask, on_delete=models.CASCADE)
    status = models.BooleanField(default=None, null=False)
