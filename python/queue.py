
class Queue:
    def __init__(self, reverse=False):
        self.items = []
        self.reverse = reverse

    @property
    def length(self):
        return len(self.items)

    @property
    def empty(self):
        if self.length:
            return True
        else:
            return False

    def enqueue(self, x):
        self.items = self.items + [x]

    def dequeue(self):
        self.items = self.items[1:]

    def import_list(self, lst):
        if not self.reverse:
            for i in sorted(lst):
                self.enqueue(i)
        else:
            for i in sorted(lst)[::-1]:
                self.enqueue(i)
