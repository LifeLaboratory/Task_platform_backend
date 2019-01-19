from task_lesson.api.helpers import names


def set_types(data):
    for k, v in data.items():
        if k in names.INTEGER_FIELDS:
            data[k] = int(v)
