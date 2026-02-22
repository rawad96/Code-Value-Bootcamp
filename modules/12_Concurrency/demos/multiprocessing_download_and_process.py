"""
DEMO - Download and Process with Multi-Processing
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
from library.image_operations import (download_image,
                                      compress_image,
                                      generate_fake_image_urls)
import timeit


NUMBER_OF_IMAGES = 5


urls = generate_fake_image_urls(NUMBER_OF_IMAGES)


def process_image(_url: str) -> str:
    image_id = download_image(_url)
    result = compress_image(image_id)
    print(f'Done Processing Image From {_url}')
    return result


if __name__ == '__main__':
    start_execution_time = timeit.default_timer()

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_image, url) for url in urls]
        
        for future in as_completed(futures):
            future.result()

    print('All images processed.')
    execution_duration = timeit.default_timer() - start_execution_time
    print(f"Execution took {execution_duration * 1000:.2f} ms")