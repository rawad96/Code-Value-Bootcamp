def extract_title_from_html(html_data: str) -> str:
    html_data_split = html_data.split("<title>")
    if len(html_data_split) > 1:
        title = html_data_split[1].split("</title>", 1)[0]
        return title
    raise ValueError("Title not found!")


if __name__ == "__main__":
    html_data = "<html><head><title>My Title</title></head><body></body></html>"
    print(extract_title_from_html(html_data))
