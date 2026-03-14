from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update as sql_update

from typing import Generic, TypeVar, Type
from ..models.base_entity import BaseEntity
from abc import ABC, abstractmethod


T_ENTITY = TypeVar("T_ENTITY", bound=BaseEntity)


class BaseRepository(ABC, Generic[T_ENTITY]):
    def __init__(self, entity_class: Type[T_ENTITY]) -> None:
        self.entity_class: Type[T_ENTITY] = entity_class

    async def create(self, item: T_ENTITY, session: AsyncSession) -> T_ENTITY:
        """Adds item and returns it."""
        session.add(item)
        await session.flush()
        await session.refresh(item)
        return item

    async def get(self, item_id: str, session: AsyncSession) -> T_ENTITY | None:
        """Return item by id"""
        return await session.get(self.entity_class, item_id)

    async def get_all(self, session: AsyncSession) -> list[T_ENTITY]:
        """Returns all items."""
        result = await session.scalars(select(self.entity_class))
        return list(result.all())

    async def update(self, item: T_ENTITY, session: AsyncSession) -> T_ENTITY:
        """Update a given item."""
        id = str(item.id)
        obj = await session.get(self.entity_class, id)
        if not obj:
            class_name = self.entity_class.__name__
            raise ValueError(f"{class_name} with id {item.id} not found")
        for key, value in vars(item).items():
            if key.startswith("_"):
                continue
            if key in ("id", "date", "is_deleted"):
                continue
            setattr(obj, key, value)

        await session.flush()
        await session.refresh(obj)

        return obj

    async def delete(self, item_id: str, session: AsyncSession) -> None:
        """Marks item as deleted."""
        stmt = (
            sql_update(self.entity_class)
            .where(self.entity_class.id == item_id)
            .values(is_deleted=True)
        )
        await session.execute(stmt)
        await session.flush()
