import time
from coroutine import ienumerate

class wait_for_seconds(ienumerate):
    def __init__(self, t:float):
        super(wait_for_seconds, self).__init__()
        self._end_time = t
        self.current = time.time()

    def move_next(self) -> bool:
        cur_time = time.time() - self.current
        if cur_time < self._end_time:
            return True
        return False

    def reset(self) -> None:
        pass
