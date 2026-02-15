from solution.extract_key_value import extract_key_value_from_log_line
import pytest


def test_extract_key_value_from_log_line():
    log_line = """2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper]
    [function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."""

    assert extract_key_value_from_log_line(log_line, "account") == "519"


def test_extract_key_value_from_log_line_second():
    log_line = """2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper]
    [function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."""

    assert extract_key_value_from_log_line(log_line, "GamePlay") == "400004380"


def test_extract_key_value_from_log_line_with_invalid_key():
    log_line = """2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper]
    [function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."""

    key = "userId"
    with pytest.raises(ValueError, match=f"{key} not found!"):
        extract_key_value_from_log_line(log_line, key)
