import time
import aiohttp
import asyncio
from typing import List
import statistics
from demos.good_and_bad_async_handlers.constants import (
    HOST,
    GOOD_HANDLER_PORT,
    BAD_HANDLER_PORT,
)
import uuid


# Constants
NUM_REQUESTS = 20
BAD_HANDLER_URL = f"http://{HOST}:{BAD_HANDLER_PORT}/get_data"
GOOD_HANDLER_URL = f"http://{HOST}:{GOOD_HANDLER_PORT}/get_data"


async def make_request(session: aiohttp.ClientSession, url: str) -> float:
    start_time = time.time()
    async with session.get(url) as response:
        response.raise_for_status()
        duration = time.time() - start_time
        print(f"Request {uuid.uuid4()} waited {duration:.3f} seconds for response")
        return duration


async def run_load_test(url: str, description: str) -> None:
    times: List[float] = []

    print(f"\nTesting {description}...")
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        requests = [make_request(session, url) for req in range(1, NUM_REQUESTS + 1)]

        results = await asyncio.gather(*requests)
        times.extend(results)

    total_time = time.time() - start_time

    print(f"Results for {description}:")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Average request time: {statistics.mean(times):.3f} seconds")
    print(f"Median request time: {statistics.median(times):.3f} seconds")
    print(f"Max request time: {max(times):.3f} seconds")
    print(f"Min request time: {min(times):.3f} seconds")
    request_per_second = NUM_REQUESTS / total_time
    print(f"Requests per second: {request_per_second:.2f}")


async def main() -> None:
    """Run load tests against both good and bad handlers."""
    print("Starting load test simulation...")

    # Test bad handler
    await run_load_test(BAD_HANDLER_URL, "Bad Handler (blocking requests)")

    # Test good handler
    await run_load_test(GOOD_HANDLER_URL, "Good Handler (async requests)")


if __name__ == "__main__":
    asyncio.run(main())
