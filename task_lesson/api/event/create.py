from task_lesson.api.event.generic import Event
import task_lesson.api.event.helpers as helpers


class EventCreate(Event):
    def __init__(self, data):
        super(EventCreate, self).__init__(data)
        if self.status == "Ok":
            self.event_id = self.get_event_id()
            if self.event_id is None:
                self.status = "Cannot get event id"

    def get_event_id(self):
        return


def event_create(data):
    new_event = EventCreate(data)
    if new_event is None or new_event.status is None:
        return helpers.ANSWER.format("Some error", data.POST["session"])
    return helpers.ANSWER.format(new_event.status, data.POST["session"])
