import time
import uvicorn
from fastapi import FastAPI
from typing import Any
import asyncio
from concurrent.futures import ProcessPoolExecutor

app = FastAPI(title="Order Processing API", version="1.0.0")

USER_FETCH_DELAY = 0.5
INVENTORY_FETCH_DELAY = 0.3
SHIPPING_FETCH_DELAY = 0.4
PAYMENT_PROCESSING_DELAY = 0.2
FIBONACCI_INDEX = 30
SERVER_PORT = 8000

executor = ProcessPoolExecutor()


def calculate_fibonacci(index: int) -> int:
    """CPU-bound operation: Calculate nth Fibonacci number recursively."""
    if index <= 1:
        return index
    return calculate_fibonacci(index - 1) + calculate_fibonacci(index - 2)


async def fetch_user_data(user_id: int) -> dict[str, Any]:
    """Simulates I/O-bound operation: Fetch user data from external service."""
    await asyncio.sleep(USER_FETCH_DELAY)
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com",
    }


async def fetch_inventory_data(product_id: int) -> dict[str, Any]:
    """Simulates I/O-bound operation: Fetch inventory from database."""
    await asyncio.sleep(INVENTORY_FETCH_DELAY)
    return {"product_id": product_id, "stock": 100, "warehouse": "Warehouse A"}


async def fetch_shipping_options(zip_code: str) -> list[dict[str, Any]]:
    """Simulates I/O-bound operation: Fetch shipping options from external service."""
    await asyncio.sleep(SHIPPING_FETCH_DELAY)
    return [
        {"method": "Standard", "cost": 5.99, "days": 5},
        {"method": "Express", "cost": 15.99, "days": 2},
        {"method": "Overnight", "cost": 29.99, "days": 1},
    ]


async def run_in_executor(executor: ProcessPoolExecutor, num: int) -> int:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, calculate_fibonacci, num)
    return result


@app.get("/process_order")
async def process_order(user_id: int, product_id: int, zip_code: str) -> dict:
    """
    Process an order by:
    1. Fetching user data
    2. Fetching inventory data
    3. Fetching shipping options
    4. Calculating shipping discount (CPU-intensive)
    """

    user, inventory, shipping = await asyncio.gather(
        fetch_user_data(user_id),
        fetch_inventory_data(product_id),
        fetch_shipping_options(zip_code),
    )

    # executor = ProcessPoolExecutor()
    fibo_result = await run_in_executor(executor=executor, num=FIBONACCI_INDEX) % 10
    discount_factor = fibo_result % 10

    await asyncio.sleep(PAYMENT_PROCESSING_DELAY)

    return {
        "user": user,
        "product": inventory,
        "shipping_options": shipping,
        "discount_percent": discount_factor,
        "status": "processed",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT)
