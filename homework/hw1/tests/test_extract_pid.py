from solution.extract_pid import extract_pid
import pytest


def test_extract_pid():
    log_line = """2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][pid:2995][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper]
    [function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."""

    assert extract_pid(log_line) == "2995"


def test_extract_pid_with_no_pid():
    log_line = """2024-04-29 15:45:00,089 INFO [name:starwars_engine.spaceship_manager.tasks][uuid:20ebf460-dcdf-4b1f-abf1-7517ef3f63c2][process:run_services_if_needed_wrapper]
    [function:run_services_if_needed][account:519][GamePlay:400004380] GamePlay's version is at least 'new' (5.2.0)."""

    with pytest.raises(ValueError, match="PID not found!"):
        extract_pid(log_line)
