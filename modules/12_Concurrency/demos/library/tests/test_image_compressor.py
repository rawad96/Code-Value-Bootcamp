import pytest
from unittest.mock import Mock
from ..image_operations import ImageCompressor


class TestImageCompressor:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.mock_logger = Mock()

    def test_compress_works(self):
        image_id = 'abcd'
        compressor = ImageCompressor(self.mock_logger)
        result = compressor.compress('abcd')
        assert self.mock_logger.log.call_count == 2
        assert isinstance(result, str)
