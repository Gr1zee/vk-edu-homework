class StackIsEmpty(Exception):
    def __init__(self, message="Стек пуст, невозможно получить элемент"):
        super().__init__(message)


class Stack():
    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        try:
            return self._stack.pop()
        except Exception:
            raise StackIsEmpty()
