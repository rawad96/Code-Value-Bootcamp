from ..repository.category_repository import CategoryRepository
from ..models.category import Category, CategoryType
from uuid import uuid4, UUID
from typing import Optional, Any

from solution.database import async_session_maker


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
    def __init__(
        self,
        repo: Optional[CategoryRepository] = None,
        session_maker=None,
    ):
        self.repo = repo or CategoryRepository()
        self.session_maker = session_maker or async_session_maker

    async def creat_category(self, category: dict[str, Any]) -> dict[str, str]:
        """Creates category and returns message."""
        async with self.session_maker() as session:
            async with session.begin():
                new_category = Category(
                    name=category["name"],
                    type=CategoryType(category["type"]),
                )
                result = await self.repo.create(new_category, session)
            return category_to_dict(result)

    async def get_all_categories(self) -> list[dict[str, Any]]:
        """Returns all categories as dicts."""
        async with self.session_maker() as session:
            categories = await self.repo.get_all(session)
            return [category_to_dict(category) for category in categories]

    async def get_by_id(self, category_id: UUID) -> dict[str, Any] | None:
        """Returns category by id or None."""
        async with self.session_maker() as session:
            category = await self.repo.get(category_id, session)
            if category is None:
                return None
            return category_to_dict(category)

    async def get_by_name(self, name: str) -> dict[str, Any] | None:
        """Returns category by name or None."""
        async with self.session_maker() as session:
            categories = await self.repo.get_all(session)
            for category in categories:
                if category.name == name:
                    return category_to_dict(category)
            return None

    async def update_category(self, category: dict[str, Any]) -> dict[str, Any]:
        """Updates category and returns it as dict."""
        async with self.session_maker() as session:
            async with session.begin():
                new_category = Category(
                    id=category["id"],
                    name=category["name"],
                    type=CategoryType(category["type"]),
                )
                updated_category = await self.repo.update(new_category, session)
            return category_to_dict(updated_category)

    async def delete_category(self, category_id: UUID) -> dict[str, str]:
        """Deletes category and returns message."""
        async with self.session_maker() as session:
            await self.repo.delete(category_id, session)
            return {"Message": "Category deleted"}
