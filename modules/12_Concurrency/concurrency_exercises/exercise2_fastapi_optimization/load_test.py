import time
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import List
import statistics
import threading

NUMBER_OF_THREADS = 20
URL = "http://localhost:8000/process_order?user_id=123&product_id=456&zip_code=12345"


def make_request(url: str) -> float:
    start_time = time.time()
    response = requests.get(url)
    response.raise_for_status()
    duration = time.time() - start_time
    return duration


def run_load_test(url: str, description: str) -> None:
    times_list: List[float] = []

    def worker() -> None:
        try:
            time_taken = make_request(url)
            times_list.append(time_taken)
        except Exception as error:
            print(f"Request failed: {error}")

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=NUMBER_OF_THREADS) as executor:
        futures = [executor.submit(worker) for exec in range(NUMBER_OF_THREADS)]
        for future in futures:
            future.result()

    total_time = time.time() - start_time
    print(f"Results for {description}:")
    print(f" - Total time: {total_time:.2f} seconds")
    print(f" - Average request time: {statistics.mean(times_list):.3f} seconds")
    request_per_second = NUMBER_OF_THREADS / total_time
    print(f" - Requests per second: {request_per_second:.2f}")


def main() -> None:
    print("Starting load test simulation...")

    run_load_test(URL, "load test")


if __name__ == "__main__":
    main()
