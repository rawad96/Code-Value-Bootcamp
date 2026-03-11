from dataclasses import dataclass
from uuid import UUID


@dataclass
class BaseEntity:
    id: UUID
    is_deleted: str
