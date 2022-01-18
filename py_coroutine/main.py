from threading import Thread
import msvcrt

import waiter
from coroutine import ienumerate, coroutine

class remove_dict_coroutine(ienumerate):
    def __init__(self, length:int) -> None:
        super(remove_dict_coroutine, self).__init__()
        self._dict = {}
        for i in range(0, length):
            self._dict[i] = i
        self._start = 0
        self._length = length
    
    def move_next(self) -> bool:
        if self._start < self._length:
            print(">>> del {}, {}".format(self._start, self._dict[self._start]))
            del self._dict[self._start]
            self._start += 1
            self.current = waiter.wait_for_seconds(1)
            return True
        return False

    def reset(self) -> None:
        pass

def main_update(c:coroutine):
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch == b'q':
                print(">>> exit")
                break
        
        c.update()


if __name__ == '__main__':
    coroutine = coroutine()

    t = Thread(target=main_update, args=[coroutine])
    t.start()

    coroutine.start(remove_dict_coroutine(100))

    t.join()

