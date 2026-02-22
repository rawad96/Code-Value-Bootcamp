from my_lru_cache import MyLruCache
import time

MAXSIZE = 3
TTL = 2.0

TIME_TO_SLEEP = 2.1

NAME = "name"
AGE = "age"

if __name__ == "__main__":
    cache = MyLruCache(maxsize=MAXSIZE, ttl=TTL)

    cache.set("user:1", {NAME: "Alice", AGE: 30})
    cache.set("user:2", {NAME: "Bob", AGE: 25})
    cache.set("user:3", {NAME: "Charlie", AGE: 35})

    print(cache.get("user:1"))
    print(cache.get("user:2"))
    print(len(cache))

    cache.set("user:4", {NAME: "David", AGE: 40})
    print(cache.get("user:3"))
    print(cache.get("user:4"))
    print(len(cache))

    cache.set("temp", "temporary_data")
    print(cache.get("temp"))
    time.sleep(TIME_TO_SLEEP)
    print(cache.get("temp"))

    print("user:1" in cache)
    print("user:999" in cache)

    cache.clear()
    print(len(cache))
