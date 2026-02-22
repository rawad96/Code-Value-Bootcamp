from collections import OrderedDict
import time
from typing import Any


class MyLruCache:
    def __init__(self, maxsize: int, ttl: float):
        self.maxsize = maxsize
        self._cache = OrderedDict()
        self.ttl = ttl

    def get(self, key: str) -> Any | None:
        if key not in self._cache:
            return None
        value, timestamp = self._cache[key]
        if time.time() - timestamp > self.ttl:
            self._cache.pop(key)
            return None
        self._cache.move_to_end(key)
        return value

    def set(self, key: str, value: Any) -> None:
        if key in self._cache:
            self._cache.move_to_end(key)
        if len(self._cache) + 1 > self.maxsize:
            self._cache.popitem(last=False)
        self._cache[key] = (value, time.time())

    def clear(self) -> None:
        self._cache.clear()

    def __len__(self) -> int:
        return len(self._cache)

    def __contains__(self, key: str) -> bool:

        if key in self._cache:
            timestamp = self._cache.get(key)[1]
            if time.time() - timestamp <= self.ttl:
                return True
        return False
