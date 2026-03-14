from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update as sql_update

from typing import Generic, TypeVar, Type
from ..models.base_entity import BaseEntity
from abc import ABC, abstractmethod


T_ENTITY = TypeVar("T_ENTITY", bound=BaseEntity)


class BaseRepository(ABC, Generic[T_ENTITY]):
    def __init__(self, entity_class: Type[T_ENTITY], session: AsyncSession) -> None:
        self.entity_class: Type[T_ENTITY] = entity_class
        self.session: AsyncSession = session

    async def create(self, item: T_ENTITY) -> T_ENTITY:
        """Adds item and returns it."""
        self.session.add(item)
        await self.session.flush()
        await self.session.refresh(item)
        return item

    async def get(self, item_id: str) -> T_ENTITY | None:
        """Return item by id"""
        return await self.session.get(self.entity_class, item_id)

    async def get_all(self) -> list[T_ENTITY]:
        """Returns all items."""
        result = await self.session.scalars(select(self.entity_class))
        return list(result.all())

    async def update(self, item: T_ENTITY) -> T_ENTITY:
        """Update a given item."""
        obj = self.session.get(self.entity_class, item.id)
        if not obj:
            class_name = self.entity_class.__name__
            raise ValueError(f"{class_name} with id {item.id} not found")
        for attr, value in vars(item).items():
            if attr in ("id", "created_at", "is_deleted"):
                continue
            setattr(obj, attr, value)

        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)

        return obj

    async def delete(self, item_id: str) -> None:
        """Marks item as deleted."""
        stmt = (
            sql_update(self.entity_class)
            .where(self.entity_class.id == item_id)
            .values(is_deleted=True)
        )
        await self.session.execute(stmt)
        await self.session.flush()

    @abstractmethod
    def _row_to_entity(self, row: dict) -> T_ENTITY:
        """Returns Entity with row data"""
        raise NotImplementedError

    @abstractmethod
    def _entity_to_row(self, entity: T_ENTITY) -> dict:
        """Returns Entity data as a row"""
        raise NotImplementedError
