

class Event():
    def __init__(self, data):
        if not self.validate_name(data.POST["name"]):
            self.status = "Invalid name"
        if not self.validate_description(data.POST["desc"]):
            self.status = "Invalid description"
        if not self.validate_picture_url(data.POST["picture_url"]):
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


class Sponsor():
    def validate_name(self, name):
        if name is None:
            return False
        return True

    def validate_picture(self, picture):
        if picture is None:
            return False
        return True