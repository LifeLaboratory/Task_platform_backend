TASK_NAME = 'name'
TASK_CATEGORY = 'category'
TASK_WEIGHT = 'weight'
TASK_FLAG = 'flag'
TASK_DESCRIPTION = 'description'
TASK_AUTHOR = 'author'
USER = 'user_id'

ADD_TASK_FIELDS = {
    TASK_NAME,
    TASK_CATEGORY,
    TASK_WEIGHT,
    TASK_FLAG,
    TASK_DESCRIPTION,
    USER
}

INTEGER_FIELDS = {
    TASK_WEIGHT,
    USER
}

# Ошибки авторизации
CreateSessionError = 'Не удалось авторизоватся. Повторите попытку позже.'
RequestValueErorr = 'Получен не корректный запрос на авторизацию'
LoginError = 'Пользователя с таким логином не существует'
PasswordError = 'Неверный пароль'