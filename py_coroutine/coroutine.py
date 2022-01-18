class ienumerate:
    def __init__(self):
        self._current = None

    def move_next(self) -> bool:
        pass

    def reset(self) -> None:
        pass

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, value):
        self._current = value

class coroutine_unit:
    def __init__(self, it:ienumerate):
        self._stack = [it]

    def move_next(self) -> bool:
        t = self._stack[-1]
        if t.move_next():
            current = t.current
            if current is not None and isinstance(current, ienumerate):
                self._stack.append(current)
            return True
        else:
            if len(self._stack) > 1:
                self._stack.pop()
                return True
        return False

    def find(self, it) -> bool:
        return it in self._stack

    def reset(self) -> None:
        self._stack = self._stack[:0]

class coroutine:
    def __init__(self):
        self._units = []
        self._buffers = []
    
    def start(self, it:ienumerate) -> None:
        self._buffers.append(it)

    def find(self, it:ienumerate) -> bool:
        for unit in self._units:
            if unit.find(it):
                return True
        return False

    def update(self) -> None:
        self._units = list(filter(lambda x: x.move_next(), self._units))
        if len(self._buffers) > 0:
            for buffer in self._buffers:
                if not self.find(buffer):
                    self._units.append(coroutine_unit(buffer))
        del self._buffers[:]
