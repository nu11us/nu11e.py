
class Stack:
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

    def push(self, x):
        self.items = [x] + self.items

    def pop(self):
        self.items = self.items[1:]

    def import_list(self, lst):
        if not self.reverse:
            for i in sorted(lst):
                self.push(i)
        else:
            for i in sorted(lst)[::-1]:
                self.push(i)
