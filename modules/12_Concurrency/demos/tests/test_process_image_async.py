import pytest
from async_download_and_process import (download_image_async,
                                        compress_image_async,
                                        process_image_async)


class TestProcessImageAsync:
    @pytest.mark.asyncio
    async def test_download_image_async(self):
        image_id = await download_image_async('https://example.com/fakeimages/image_1.jpg')
        assert isinstance(image_id, str)

    @pytest.mark.asyncio
    async def test_compress_image_async(self):
        compressed_image = await compress_image_async('image_id')
        assert isinstance(compressed_image, str)

    @pytest.mark.asyncio
    async def test_process_image_async(self):
        result = await process_image_async('https://example.com/fakeimages/image_1.jpg')
        assert isinstance(result, str)
