from solution.extract_html_content import extract_title_from_html
import pytest


def test_extract_html_content():
    html_data = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>rawad bader</title>
    <meta name="description" content="Test HTML document for unit testing.">
    <meta name="author" content="rawad bader">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>rawad bader</h1>
    <p>This is a sample HTML page for testing purposes.</p>
</body>
</html>

"""
    expected_title = "rawad bader"

    assert extract_title_from_html(html_data) == expected_title


def test_extract_html_content_with_no_title():
    html_data = "<html><head></head><body></body></html>"
    with pytest.raises(ValueError, match="Title not found!"):
        extract_title_from_html(html_data)
