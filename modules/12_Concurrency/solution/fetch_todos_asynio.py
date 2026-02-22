import aiohttp
import asyncio
from typing import Any

URL = "https://jsonplaceholder.typicode.com/todos/{}"

NUMBER_OF_TODOS = 20


async def fetch_todo(session: aiohttp.ClientSession, todo_id: int) -> dict[str, Any]:
    async with session.get(URL.format(todo_id)) as response:
        response.raise_for_status()
        return await response.json()


async def main() -> None:
    print(f"Fetching {NUMBER_OF_TODOS} TODO items using asyncio and aiohttp...")
    start_time = asyncio.get_event_loop().time()

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_todo(session, todo_id) for todo_id in range(1, NUMBER_OF_TODOS + 1)
        ]

        for task in asyncio.as_completed(tasks):
            todo = await task
            print(f"TODO {todo['id']}: {todo['title']}")

    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    avg_time = total_time / NUMBER_OF_TODOS

    print(f"\nTotal time: {total_time:.2f} seconds")
    print(f"Average time per TODO: {avg_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
