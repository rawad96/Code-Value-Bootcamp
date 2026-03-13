from solution.models.category import CategoryType
from solution.services.category_service import CategoryService

NAME = "name"
TYPE = "type"


def seed_categories() -> None:
    service = CategoryService()
    default_categories = [
        {NAME: "Salary", TYPE: CategoryType.INCOME},
        {NAME: "Freelance", TYPE: CategoryType.INCOME},
        {NAME: "Rent", TYPE: CategoryType.EXPENSE},
        {NAME: "Groceries", TYPE: CategoryType.EXPENSE},
        {NAME: "Utilities", TYPE: CategoryType.EXPENSE},
        {NAME: "Entertainment", TYPE: CategoryType.EXPENSE},
        {NAME: "Transfer In", TYPE: CategoryType.INCOME},
        {NAME: "Transfer Out", TYPE: CategoryType.EXPENSE},
    ]

    existing_categories = service.get_all_categories()
    existing_names = [category["name"] for category in existing_categories]

    for category in default_categories:
        if category["name"] not in existing_names:
            service.creat_category(category)
