from task_lesson.api.helpers import names


def set_types(data):
    """
    Метод преобразует типы в словаре
    :param data:
    :return:
    """
    for k, v in data.items():
        if k in names.INTEGER_FIELDS:
            data[k] = int(v)


def check_dict(data, check_list):
    """
    Метод проверяет входные данные по заданному формату.
    Возвращает словарь проверенных полей и признак, всё ли поля заполнены
    :param data:
    :param check_list:
    :return:
    """
    check = dict()
    checked = True
    for key in check_list:
        if data.get(key, None):
            check[key] = data[key]
        else:
            check[key] = 'Поле не заполнено'
            checked = False
    if checked:
        set_types(check)
    return check, checked
