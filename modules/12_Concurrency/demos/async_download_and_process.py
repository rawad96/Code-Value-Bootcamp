"""

DEMO - Same Download and Compress using asyncio, ThreadPoolExecutor,
       and ProcessPoolExecutor

"""

import asyncio

from library.image_operations import (download_image,
                                      compress_image,
                                      generate_fake_image_urls)
import timeit
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


NUMBER_OF_IMAGES = 5
MAX_WORKERS = NUMBER_OF_IMAGES


urls = generate_fake_image_urls(NUMBER_OF_IMAGES)


async def run_in_executor(executor, func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    with executor as pool:
        print(f'Running {func.__name__} in {executor.__class__.__name__}...')
        result = await loop.run_in_executor(pool, func, *args, **kwargs)
    return result


async def download_image_async(_url: str) -> str:
    executor = ThreadPoolExecutor()
    return await run_in_executor(executor, download_image, _url)


async def compress_image_async(image_id: str) -> str:
    executor = ProcessPoolExecutor()
    return await run_in_executor(executor, compress_image, image_id)


async def process_image_async(_url: str) -> str:
    image_id = await download_image_async(_url)
    result = await compress_image_async(image_id)
    print(f'Done Processing Image From {_url}')
    return result


async def process_all_async():

    coroutines = [process_image_async(url) for url in urls]
    results = await asyncio.gather(*coroutines)
    return results


async def main():
    start_execution_time = timeit.default_timer()
    await process_all_async()
    print('All images processed.')
    execution_duration = timeit.default_timer() - start_execution_time
    print(f"Execution took {execution_duration * 1000:.2f} ms")


if __name__ == '__main__':
    asyncio.run(main())
