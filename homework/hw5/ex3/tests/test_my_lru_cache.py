from solution.my_lru_cache import MyLruCache
import time

MAXSIZE = 3
TTL = 2.0

TIME_TO_SLEEP = 2.1

NAME = "name"
AGE = "age"

USER1 = "user:1"
USER2 = "user:2"
USER3 = "user:3"
USER4 = "user:4"

ALICE = "Alice"


def test_basic_operations() -> None:
    cache = MyLruCache(maxsize=MAXSIZE, ttl=TTL)

    cache.set(USER1, {NAME: ALICE, AGE: 30})
    assert cache.get(USER1) == {NAME: ALICE, AGE: 30}

    assert cache.get("non_existent") is None

    cache.set(USER2, {NAME: "Alice Updated", AGE: 31})
    assert cache.get(USER2) == {NAME: "Alice Updated", AGE: 31}


def test_lru_eviction() -> None:
    cache = MyLruCache(maxsize=MAXSIZE, ttl=TTL)

    cache.set(USER1, {NAME: ALICE, AGE: 30})
    cache.set(USER2, {NAME: "Bob", AGE: 25})
    cache.set(USER3, {NAME: "Charlie", AGE: 35})

    assert cache.get(USER1) == {NAME: ALICE, AGE: 30}

    cache.set(USER4, {NAME: "David", AGE: 40})

    assert cache.get(USER2) is None
    assert cache.get(USER3) == {NAME: "Charlie", AGE: 35}
    assert cache.get(USER4) == {NAME: "David", AGE: 40}


def test_ttl_expiration() -> None:
    cache = MyLruCache(maxsize=MAXSIZE, ttl=TTL)

    cache.set("temp", "temporary_data")
    assert cache.get("temp") == "temporary_data"

    time.sleep(TIME_TO_SLEEP)
    assert cache.get("temp") is None


def test_edge_cases() -> None:
    cache = MyLruCache(maxsize=1, ttl=TTL)
    cache.set(USER1, {NAME: ALICE, AGE: 30})
    assert cache.get(USER1) == {NAME: ALICE, AGE: 30}
    cache.set(USER2, {NAME: "Bob", AGE: 25})
    assert cache.get(USER1) is None
