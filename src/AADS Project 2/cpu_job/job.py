class Job:
    __slots__ = '_name', '_length', '_waiting_slice_time'

    def __init__(self, name, length):
        if 1 <= length <= 100:
            self._name = name
            self._length = length
            self._waiting_slice_time = 0
        else:
            raise ValueError("Length out of bound")

    def get_name(self):
        return self._name

    def get_length(self):
        return self._length

    def get_waiting_slice_time(self):
        return self._waiting_slice_time

    def set_waiting_slice_time(self, waiting_slice_time):
        self._waiting_slice_time = waiting_slice_time

    def set_length(self, length):
        self._length=length
