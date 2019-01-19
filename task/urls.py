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
from task_lesson.api.task.task import AddTask
from task_lesson.api.team.create import CreateTeam
from task_lesson.api.team.edit import EditTeam
from task_lesson.api.authorization.get_session import Authorization as Auth
from task_lesson.api.registration.registration_user import RegistrationUser as RegiUser
from task_lesson.api.registration.event_registration_team import EventRegistrationTeam as RegiOnEvent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/create/', CreateTeam().create),
    path('team/edit/', EditTeam().edit),
    path('add_task/', AddTask().add_task),
    path('auth/', Auth.get_session),
    path('registration/', RegiUser.registation),
    path('event_registration_team/', RegiOnEvent.registation)
]
