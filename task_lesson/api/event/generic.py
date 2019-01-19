from task_lesson.api.helpers import names

class Event():
    def __init__(self, data):
        raw_data = self.parse_data(data, names.CREATE_EVENT_FIELDS)
        if self.validate_name(raw_data[names.EVENT_NAME]) is not None:
            self.status = "Invalid name"
        elif self.validate_description(raw_data[names.EVENT_DESC]) is not None:
            self.status = "Invalid description"
        elif self.validate_picture_url(raw_data[names.EVENT_PICTURE_URL]) is not None:
            self.status = "Invalid picture url"

        self.name = data.POST["name"]
        self.desc = data.POST["desc"]
        self.picture_url = data.POST["picture_url"]
        self.status = "Ok"

    def validate_name(self, name):
         if name is None:
             return False
         return True

    def validate_description(self, desc):
         if desc is None:
             return False
         return True

    def validate_picture_url(self, picture_url):
         if picture_url is None:
             return False
         return True

    def parse_data(self, responce, fields):
        """
        Метод проверяет в запросе наличие необходимых полей и возвращает словарь с данными
        :param responce:
        :return: dict
        """
        data = dict()
        for k in fields:
            field = responce.POST.get(k, None)
            if field is not None:
                data[k] = field
        return data

class Sponsor():
    def validate_name(self, name):
        if name is None:
            return False
        return True

    def validate_picture(self, picture):
        if picture is None:
            return False
        return True