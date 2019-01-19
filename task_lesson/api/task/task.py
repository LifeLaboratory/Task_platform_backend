class Task:
    """
    Родительский класс для тасков
    """
    def __init__(self):
        self.row_data = None

    @staticmethod
    def parse_data(responce, fields):
        """
        Метод проверяет в запросе наличие необходимых полей и возвращает словарь с данными
        :param responce:
        :return: dict
        """
        data = dict()
        for k in fields:
            field = responce.get(k, None)
            if field is not None:
                data[k] = field
        if data == {}:
            return None
        return data


