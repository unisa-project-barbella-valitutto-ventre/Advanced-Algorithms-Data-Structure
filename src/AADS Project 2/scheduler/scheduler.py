from heap_priority_queue.heap_priority_queue import HeapPriorityQueue
from cpu_job.job import Job

class Scheduler (HeapPriorityQueue):

    #------------------------------ nested Locator class ------------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'                 # add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index = j

        def get_value(self):
            return self._value

        def get_key(self):
            return self._key

    #------------------------------ nonpublic behaviors ------------------------------
    # override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i,j)                   # perform the swap
        self._data[i]._index = i             # reset locator index (post-swap)
        self._data[j]._index = j             # reset locator index (post-swap)

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def _add_job(self, key, value):
        token = self.Locator(key, value, len(self._data)) # initiaize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def _update(self, loc, newkey):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = newkey
        self._bubble(j)

    #------------------------------ public behaviors ------------------------------

    __slots__ = '_max_waiting_time', '_scheduled'

    def __init__(self, max_waiting_time=4):
        super().__init__()
        self._max_waiting_time = max_waiting_time
        self._scheduled = None

    def add(self, job, priority):
        if not isinstance(job, Job):
            raise TypeError("The job is not valid.")
        if -20<=priority<=19:
            token = self._add_job(priority, job)
            print("Add job " + job.get_name() + " with length " + str(job.get_length()) + " and priority ",
                  priority)
            return token
        else:
            raise ValueError("Priority not valid")

    def assign_job(self):
        if self._scheduled is None and not self.is_empty():
            priority, job = self.remove_min()
            self._scheduled = job
            print("Job " + self._scheduled.get_name() + " with priority " + str(priority) + " assigned to the CPU")

    def update_job_priorities(self):
        if not self.is_empty():
            for loc in self._data:
                job = loc.get_value()
                increased_waiting_slice_time = job.get_waiting_slice_time()+1
                if increased_waiting_slice_time < self._max_waiting_time:
                    job.set_waiting_slice_time(increased_waiting_slice_time)
                else:
                    job.set_waiting_slice_time(0)
                    if loc.get_key() > -20:
                        self._update(loc, (loc.get_key())-1)

    def update_scheduled_job(self):
        if self._scheduled is not None:
            print("The job " + self._scheduled.get_name() + " is currently running on the CPU. Remaining time: " + str(
                self._scheduled.get_length()))
            self._scheduled.set_length(self._scheduled.get_length() - 1)
            if self._scheduled.get_length() == 0:
                print("Job " + self._scheduled.get_name() + " complete!")
                self._scheduled = None
        else:
            print("No job currently running on the CPU.")
