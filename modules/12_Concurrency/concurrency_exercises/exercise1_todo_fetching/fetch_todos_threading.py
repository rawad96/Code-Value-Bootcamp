import requests
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from typing import Any

URL = "https://jsonplaceholder.typicode.com/todos/{id}"

NUMBER_OF_TODOS = 20


def fetch_todo(todo_id: int) -> dict[str, Any]:
    response = requests.get(URL.format(id=todo_id))
    return response.json()


if __name__ == "__main__":
    print(f"Fetching {NUMBER_OF_TODOS} TODO items using ThreadPoolExecutor...")
    start_time = time.time()

    results = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_id = {
            executor.submit(fetch_todo, todo_id): todo_id
            for todo_id in range(1, NUMBER_OF_TODOS + 1)
        }
        for future in as_completed(future_to_id):
            todo = future.result()
            results.append(todo)
            print(f"TODO {future_to_id[future]}: {todo['title']}")

    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / NUMBER_OF_TODOS

    print("\nSummary:")
    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Average time per request: {avg_time:.3f} seconds")
