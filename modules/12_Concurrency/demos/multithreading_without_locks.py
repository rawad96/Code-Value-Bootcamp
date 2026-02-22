from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import timeit

start_execution_time = timeit.default_timer()


DEFAULT_STEP = 50
THREADS = 10


class Counter:
    def __init__(self, step: int = DEFAULT_STEP):
        self._count = 0
        self._step = step

    @property
    def count(self) -> int:
        return self._count

    def increment_to_step(self) -> None:
        for i in range(self._step):
            current = self._count
            print(f"Current thread ID: {threading.get_ident()} at iteration: {i} Counter: {current}")
            current += 1
            self._count = current


# Create an instance of Counter
counter = Counter()

with ThreadPoolExecutor(max_workers=THREADS) as executor:
    futures = [executor.submit(counter.increment_to_step) for _ in range(THREADS)]

    for future in as_completed(futures):
        future.result()

print(f"Final count (without locks): {counter.count}) ")
execution_duration = timeit.default_timer() - start_execution_time
print(f"Execution took {execution_duration * 1000:.2f} ms")
