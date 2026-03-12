from solution.api.api_client import get, post, delete
from solution.ui.ui_utils import choose_category


def view_categories():
    categories = get("/categories/")

    for cat in categories:
        print(f"{cat['name']} | {cat['type']}")


def add_category():
    name = input("Category name: ")
    category_type = input("Type (income/expense): ")
    post("/categories/", {"name": name, "type": category_type})

    print("Category created")


def delete_category():
    category_id = choose_category()
    delete(f"/categories/{category_id}")

    print("Category deleted")
