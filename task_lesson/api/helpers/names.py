TASK = 'task'
TASK_NAME = 'name'
TASK_CATEGORY = 'category'
TASK_WEIGHT = 'weight'
TASK_FLAG = 'flag'
TASK_DESCRIPTION = 'description'
TASK_AUTHOR = 'author'
EVENT = 'event'
USER = 'user'
ANSWER = 'answer'
SESSION = 'session'
EVENT_NAME = 'name'
EVENT_DESC = 'desc'
EVENT_PICTURE_URL = 'picture_url'

TEAM_ID = 'team'
TEAM_NAME = 'name'
TEAM_DESCRIPTION = 'description'
TEAM_PICTURE = 'pictureurl'
TEAM_USER_ID = 'user_id'


ADD_TASK_FIELDS = {
    TASK_NAME,
    TASK_CATEGORY,
    TASK_WEIGHT,
    TASK_FLAG,
    TASK_DESCRIPTION,
    USER
}

EVENT_TASK_FIELDS = {
    EVENT
}

TASK_FIELDS = {
    TASK,
    TASK_NAME,
    TASK_CATEGORY,
    TASK_WEIGHT,
    TASK_DESCRIPTION,
    USER
}

VIEW_TASK_FIELDS = {
    EVENT,
    TASK_CATEGORY
}

PASS_TASK_FIELDS = {
    EVENT,
    TASK,
    TASK_FLAG,
    USER
}

ADD_TEAM_FIELDS = {
    TEAM_NAME,
    TEAM_PICTURE
}

EDIT_TEAM_FIELDS = {
    TEAM_ID,
    TEAM_NAME,
    TEAM_PICTURE
}

INTEGER_FIELDS = {
    TASK_WEIGHT,
    USER,
    EVENT,
    TASK
}

STRING_FIELDS = {
    TASK_CATEGORY
}

CREATE_EVENT_FIELDS = {
    EVENT_NAME,
    EVENT_DESC,
    EVENT_PICTURE_URL
}
# Ошибки авторизации
answer = 'answer'
CreateSessionError = 'Не удалось авторизоватся. Повторите попытку позже.'
RequestValueErorr = 'Получен не корректный запрос на авторизацию'
LoginError = 'Пользователя с таким логином не существует'
PasswordError = 'Неверный пароль'
NameTeamIsNotEmpty = 'Такое название команды уже существует'
EventNameError = 'Получено некорректное имя события'
EventDescriptionError = 'Получено некорректное описание события'
EventPictureUrlError = 'Получен некорректный URL картинки'
AuthorizationError = 404
AllGood = 200
ServerError = 500

TimeOutSession = 6000
ERROR_ADD_TASK = 'Ошибка добавления таска'
ERROR_REQUEST_DATABASE = 'Ошибка запроса к бд'
OK = 'OK'
