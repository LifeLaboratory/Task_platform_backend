from task_lesson.api.event.generic import Event
import task_lesson.api.event.helpers as helpers


class EventUpdate(Event):
    def __init__(self, data):
        super(EventUpdate, self).__init__(data)
        if self.status == "Ok":
            self.event_id = self.get_event_id(data)
            if self.event_id is None:
                self.status = "Cannot get event id"
            else:
                self.permition_is_true = self.check_permition()
        if self.permition_is_true is not None:
            self.apply_changes(data)



    def get_event_id(self, data):
        return

    def check_permition(self, data):
        return

    def apply_changes(self, data):
        return


def event_update(data):
    new_event = EventUpdate(data)
    if new_event is None or new_event.status is None:
        return helpers.ANSWER.format("Some error", data.POST.session)
    return helpers.ANSWER.format(new_event.status, data.POST.session)

