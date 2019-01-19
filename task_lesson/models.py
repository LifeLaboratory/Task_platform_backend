from django.db import models

# Create your models here.


class User(models.Model):
    user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.user


class Role(models.Model):
    role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)


class Team(models.Model):
    team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pictureurl = models.CharField(max_length=128)


class TeamUser(models.Model):
    teamuser = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.BooleanField(default=None)


class Event(models.Model):
    event = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    pictureurl = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)


class EventTeamUser(models.Model):
    eventteamuser = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    teamuser = models.ForeignKey(TeamUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Task(models.Model):
    task = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    weight = models.FloatField(max_length=128)
    flag = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)
    # Автор задания
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class EventTask(models.Model):
    eventtask = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class Sponsor(models.Model):
    sponsor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    pictureurl = models.CharField(max_length=128)


class EventSponsor(models.Model):
    eventsponsor = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)


class Hint(models.Model):
    hint = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048)


class Solution(models.Model):
    solution = models.AutoField(primary_key=True)
    teamuser = models.ForeignKey(TeamUser, on_delete=models.CASCADE)
    eventtask = models.ForeignKey(EventTask, on_delete=models.CASCADE)
    status = models.BooleanField()
