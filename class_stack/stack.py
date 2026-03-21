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

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        if not self._stack:
            return "Stack()"
        _s = ""
        for _el in self._stack[:-1]:
            _s += f"{_el}, "
        _s += str(self._stack[-1])
        return f"Stack({_s})"

    def __repr__(self):
        return f"Stack({self._stack})"

    def __iter__(self):
        for elem in self._stack:
            yield elem

    def __contains__(self, value):
        return value in self._stack

    def __getitem__(self, index):
        return self._stack[index]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stack.clear()
        return None

    def __eq__(self, other):
        return self._stack == other._stack
