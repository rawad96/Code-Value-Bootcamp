import time
import uuid
from .default_logger import DefaultLogger


PROCESSING_TIME = 1
COMPRESSION_LEVEL = 10**6
NUMBER_OF_IMAGES = 5
default_logger = DefaultLogger


class ImageCompressor:

    def __init__(self, 
                 logger=default_logger,
                 compression_level = COMPRESSION_LEVEL) -> None:
        self.__logger = logger
        self.__compression_level = compression_level

    def compress(self, image_id: str) -> str:
        self.__logger.log(f'Processing Image {image_id}')
        result = self.__heavy_computation(self.__compression_level)
        self.__logger.log(f'Compression Complete. Result: {result}')
        return result

    @staticmethod
    def __fib(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def __heavy_computation(self, cls=None) -> str:
        # A function to perform heavy computation
        start_time = time.time()
        result = self.__fib(self.__compression_level)
        return f'{str(time.time())}-{str(uuid.uuid4())}'


def download_image(url: str):
    default_logger.log(f'Downloading from {url} ...')
    time.sleep(PROCESSING_TIME)
    return str(uuid.uuid4())


def compress_image(image_id: str):
    return ImageCompressor().compress(image_id)


def generate_fake_image_urls(total=NUMBER_OF_IMAGES):
    base_url = "https://example.com/fakeimages"
    return [f"{base_url}/image_{i}.jpg" for i in range(1, total + 1)]