from ..repository.category_repository import CategoryRepository
from ..models.category import Category, CategoryType
from uuid import uuid4, UUID
from typing import Optional


class CategoryService:
    def __init__(self, repo: Optional[CategoryRepository] = None):
        self.repo = repo or CategoryRepository()

    def creat_category(self, category: Category) -> dict[str, str]:
        new_category = Category(
            id=uuid4(),
            name=category.name,
            type=category.type,
        )
        self.repo.create(new_category)
        return {"Message": "Category created"}

    def get_all_categories(self) -> list[Category]:
        categories = self.repo.get_all()
        return categories

    def get_by_id(self, category_id: UUID) -> Category:
        category = self.repo.get(category_id)
        return category

    def get_by_name(self, name: str) -> Category:
        categories = self.repo.get_all()
        for category in categories:
            if category.name == name:
                return category

    def update_category(self, category: Category) -> Category:
        updated_category = self.repo.update(category)

        return updated_category

    def delete_category(self, category_id: UUID) -> dict[str, str]:
        self.repo.delete(category_id)

        return {"Message": "Category deleted"}
