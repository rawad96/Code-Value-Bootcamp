from solution.models.category import CategoryType
from solution.services.category_service import CategoryService


def seed_categories():
    service = CategoryService()
    default_categories = [
        {"name": "Salary", "type": CategoryType.INCOME},
        {"name": "Freelance", "type": CategoryType.INCOME},
        {"name": "Rent", "type": CategoryType.EXPENSE},
        {"name": "Groceries", "type": CategoryType.EXPENSE},
        {"name": "Utilities", "type": CategoryType.EXPENSE},
        {"name": "Entertainment", "type": CategoryType.EXPENSE},
        {"name": "Transfer In", "type": CategoryType.INCOME},
        {"name": "Transfer Out", "type": CategoryType.EXPENSE},
    ]

    existing_categories = service.get_all_categories()
    existing_names = [category["name"] for category in existing_categories]

    for category in default_categories:
        if category["name"] not in existing_names:
            service.creat_category(category)
