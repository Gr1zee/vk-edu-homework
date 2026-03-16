from Exception import Exception


class StackIsEmpty(Exception):
    def __init__(self, message="Стек пуст, невозможно получить элемент"):
        super.__init__(message)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        try:
            return self.stack.pop()
        except Exception:
            raise StackIsEmpty()
