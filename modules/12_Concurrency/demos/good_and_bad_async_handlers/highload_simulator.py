import time
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List
import statistics
import threading
from constants import HOST, GOOD_HANDLER_PORT, BAD_HANDLER_PORT


# Constants
NUM_THREADS = 20
BAD_HANDLER_URL = f"http://{HOST}:{BAD_HANDLER_PORT}/get_data"
GOOD_HANDLER_URL = f"http://{HOST}:{GOOD_HANDLER_PORT}/get_data"


def make_request(url: str) -> float:
    """Make a single request and return the time taken."""
    start_time = time.time()
    response = requests.get(url)
    response.raise_for_status()
    duration = time.time() - start_time
    print(f'Client {threading.get_ident()} waited {duration:.3f} seconds for response')
    return duration

def run_load_test(url: str, description: str) -> None:
    """Run load test against specified URL and print results."""
    times: List[float] = []
    
    def worker() -> None:
        try:
            time_taken = make_request(url)
            times.append(time_taken)
        except Exception as e:
            print(f"Request failed: {e}")

    print(f"\nTesting {description}...")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(worker) for _ in range(NUM_THREADS)]
        # Wait for all futures to complete
        for future in futures:
            future.result()
    
    total_time = time.time() - start_time
    
    print(f"Results for {description}:")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Average request time: {statistics.mean(times):.3f} seconds")
    print(f"Median request time: {statistics.median(times):.3f} seconds")
    print(f"Max request time: {max(times):.3f} seconds")
    print(f"Min request time: {min(times):.3f} seconds")
    print(f"Requests per second: {NUM_THREADS/total_time:.2f}")

def main() -> None:
    """Run load tests against both good and bad handlers."""
    print("Starting load test simulation...")
    
    # Test bad handler
    run_load_test(BAD_HANDLER_URL, "Bad Handler (blocking requests)")
    
    # Test good handler
    run_load_test(GOOD_HANDLER_URL, "Good Handler (async requests)")


if __name__ == "__main__":
    main()