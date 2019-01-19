TASK_NAME = 'name'
TASK_CATEGORY = 'category'
TASK_WEIGHT = 'weight'
TASK_FLAG = 'flag'
TASK_DESCRIPTION = 'description'
TASK_AUTHOR = 'author'
EVENT = 'event'
USER = 'user_id'
ANSWER = 'answer'
SESSION = 'session'

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
    EVENT
}

# Ошибки авторизации
answer = 'answer'
CreateSessionError = 'Не удалось авторизоватся. Повторите попытку позже.'
RequestValueErorr = 'Получен не корректный запрос на авторизацию'
LoginError = 'Пользователя с таким логином не существует'
PasswordError = 'Неверный пароль'
NameTeamIsNotEmpty = 'Такое название команды уже существует'
AuthorizationError = 404
AllGood = 200
ServerError = 500

TimeOutSession = 6000
ERROR_ADD_TASK = 'Ошибка добавления таска'
ERROR_REQUEST_DATABASE = 'Ошибка запроса к бд'
OK = 'OK'
