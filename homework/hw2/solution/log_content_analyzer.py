def analyze_log_content(log_content: str) -> dict:
    returned_dict = dict()
    returned_dict["Error"] = (
        len(log_content.split("ERROR")) - 1
    )  # -1 because split will always return a list with at least one element.
    returned_dict["Warning"] = len(log_content.split("WARNING")) - 1
    returned_dict["Info"] = len(log_content.split("INFO")) - 1

    return returned_dict


if __name__ == "__main__":
    log_content = """
2024-04-29 15:45:00,089 INFO [name:starwars_engine][pid:2995] Message one
2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
2024-04-29 15:45:08,111 /var/log/apache2/server.access.log 172.18.0.12 - - "POST /api/command/?201dfd68-e48d-587b-e715-3ff83ef3af19 HTTP/1.1" 200
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:46:00,789 INFO [name:starwars_engine][pid:2998] All systems go
"""
    print(analyze_log_content(log_content))
