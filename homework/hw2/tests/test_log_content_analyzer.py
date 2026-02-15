from solution.log_content_analyzer import analyze_log_content


def test_analyze_log_content() -> None:
    log_content = """
2024-04-29 15:45:00,089 INFO [name:starwars_engine][pid:2995] Message one
2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
2024-04-29 15:45:08,111 /var/log/apache2/server.access.log 172.18.0.12 - - "POST /api/command/?201dfd68-e48d-587b-e715-3ff83ef3af19 HTTP/1.1" 200
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:46:00,789 INFO [name:starwars_engine][pid:2998] All systems go
"""
    assert analyze_log_content(log_content) == {"Error": 1, "Warning": 1, "Info": 2}


def test_analyze_log_content_second_check() -> None:
    log_content = """
2024-04-29 15:45:00,089 INFO [name:starwars_engine][pid:2995] Message one
2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
2024-04-29 15:45:08,111 /var/log/apache2/server.access.log 172.18.0.12 - - "POST /api/command/?201dfd68-e48d-587b-e715-3ff83ef3af19 HTTP/1.1" 200
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:46:00,789 INFO [name:starwars_engine][pid:2998] All systems go
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
"""
    assert analyze_log_content(log_content) == {"Error": 3, "Warning": 2, "Info": 2}
