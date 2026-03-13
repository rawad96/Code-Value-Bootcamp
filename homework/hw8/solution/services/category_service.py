from ..repository.category_repository import CategoryRepository
from ..models.category import Category, CategoryType
from uuid import uuid4, UUID
from typing import Optional, Any


def category_to_dict(category: Category) -> dict[str, Any]:
    """Returns category as dict."""
    return {
        "id": str(category.id),
        "name": category.name,
        "type": (
            category.type.value if hasattr(category.type, "value") else category.type
        ),
        "is_deleted": category.is_deleted,
    }


class CategoryService:
    def __init__(self, repo: Optional[CategoryRepository] = None):
        self.repo = repo or CategoryRepository()

    def creat_category(self, category: dict[str, Any]) -> dict[str, str]:
        """Creates category and returns message."""
        new_category = Category(
            id=uuid4(),
            name=category["name"],
            type=CategoryType(category["type"]),
            is_deleted="false",
        )
        self.repo.create(new_category)
        return {"Message": "Category created"}

    def get_all_categories(self) -> list[dict[str, Any]]:
        """Returns all categories as dicts."""
        categories = self.repo.get_all()
        return [category_to_dict(category) for category in categories]

    def get_by_id(self, category_id: UUID) -> dict[str, Any] | None:
        """Returns category by id or None."""
        category = self.repo.get(category_id)
        if category is None:
            return None
        return category_to_dict(category)

    def get_by_name(self, name: str) -> dict[str, Any] | None:
        """Returns category by name or None."""
        categories = self.repo.get_all()
        for category in categories:
            if category.name == name:
                return category_to_dict(category)
        return None

    def update_category(self, category: dict[str, Any]) -> dict[str, Any]:
        """Updates category and returns it as dict."""
        new_category = Category(
            id=category["id"],
            name=category["name"],
            type=CategoryType(category["type"]),
            is_deleted="false",
        )
        updated_category = self.repo.update(new_category)

        return category_to_dict(updated_category)

    def delete_category(self, category_id: UUID) -> dict[str, str]:
        """Deletes category and returns message."""
        self.repo.delete(category_id)

        return {"Message": "Category deleted"}
