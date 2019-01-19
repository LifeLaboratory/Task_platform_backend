from task_lesson.api.event.generic import Event
import task_lesson.api.event.helpers as helpers


class EventUpdate(Event):
    def __init__(self, data):
        super(EventUpdate, self).__init__(data)

    def get_event_id(self):
        return


def event_update(data):
    new_event = EventUpdate(data)
    if new_event is None or new_event.status is None:
        return helpers.ANSWER.format("Some error", data.POST.session)
    return helpers.ANSWER.format(new_event.status, data.POST.session)

