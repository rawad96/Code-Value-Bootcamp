import requests
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
from typing import Any

URL = "https://jsonplaceholder.typicode.com/todos/{}"

NUMBER_OF_TODOS = 20


def fetch_todo(todo_id: int) -> dict[str, Any]:
    response = requests.get(URL.format(todo_id))
    response.raise_for_status()
    return response.json()


def main() -> None:
    print(f"Fetching {NUMBER_OF_TODOS} TODO items using ProcessPoolExecutor...")

    start_time = time.time()

    results = []

    with ProcessPoolExecutor(max_workers=8) as executor:
        future_to_id = {
            executor.submit(fetch_todo, todo_id): todo_id
            for todo_id in range(1, NUMBER_OF_TODOS + 1)
        }

        for future in as_completed(future_to_id):
            todo = future.result()
            results.append(todo)
            print(f"TODO {future_to_id[future]}: {todo['title']}")

    total_time = time.time() - start_time
    avg_time = total_time / NUMBER_OF_TODOS

    print("\nSummary:")
    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Average time per request: {avg_time:.3f} seconds")


if __name__ == "__main__":
    main()
