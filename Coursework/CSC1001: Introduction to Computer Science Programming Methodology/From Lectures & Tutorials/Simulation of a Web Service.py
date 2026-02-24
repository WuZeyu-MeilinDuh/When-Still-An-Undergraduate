from Queue import Queue

class WebService:
    default_capacity = 5

    def __init__(self):
        self.nameQ = Queue()
        self.timeQ = Queue()

    def take_arrive(self, name, time):
        if self.nameQ.__len__() < WebService.default_capacity:
            self.nameQ.enqueue(name)
            self.timeQ.enqueue(time)
            print(name + ' is to be processed.')
        else:
            print('The waiting list is full. The work ' + name + ' is automatically dropped.')

    def take_process(self):
        if self.nameQ.is_empty():
            print('No work to be processed.')
        else:
            name_to = self.nameQ.dequeue()
            time_to = self.timeQ.dequeue()
            print(name_to + ' has been processed and the time consumption was ' + time_to)