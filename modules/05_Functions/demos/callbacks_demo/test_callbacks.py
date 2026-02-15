import pytest
from unittest.mock import patch
from callbacks import call_microsoft


class TestCallbacks:

    @patch('callbacks.my_logger')
    def test_logger_called_with_right_args(self, logger_mock):
        token = "current_token"
        data = call_microsoft(token)
        logger_mock.log.asser_called_with(str(data))
        assert data is not None
