from solution.api.api_client import get, post, delete
from solution.ui.ui_utils import choose_category


def view_categories() -> None:
    """Shows all categories."""
    categories = get("/categories/")

    print("\n-----All Categories-----")
    for cat in categories:
        print(f"{cat['name']} | {cat['type']}")


def add_category() -> None:
    """Adds new category."""
    name = input("Category name: ")
    category_type = input("Type (income/expense): ")
    post("/categories/", {"name": name, "type": category_type})

    print("\nCategory created")


def delete_category() -> None:
    """Deletes category."""
    category_id = choose_category()
    delete(f"/categories/{category_id}")

    print("\nCategory deleted")
