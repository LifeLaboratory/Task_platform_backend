"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_lesson.api.task.create_task import CreateTask
from task_lesson.api.team.create import CreateTeam
from task_lesson.api.team.edit import EditTeam
from task_lesson.api.task.view_task import ViewTask
from task_lesson.api.task.pass_task import PassTask
from task_lesson.api.authorization.get_session import Authorization as Auth
from task_lesson.api.event.show import ShowEvent
from task_lesson.api.registration.registration_user import RegistrationUser as RegiUser
from task_lesson.api.registration.event_registration_team import EventRegistrationTeam as RegiOnEvent


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/team/create/', CreateTeam().create),
    path('api/team/edit/', EditTeam().edit),
    path('api/task/create/', CreateTask().create_task),
    path('api/task/view/', ViewTask().view_task),
    path('api/task/pass/', PassTask().pass_task),
    path('api/auth/', Auth.get_session),
    path('api/registration/user', RegiUser.registation),
    path('api/event/registration/team/', RegiOnEvent.registation),
    path('api/event/list/', ShowEvent().get_list_event)
]
