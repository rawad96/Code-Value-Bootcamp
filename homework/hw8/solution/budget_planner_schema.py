from pydantic import BaseModel


class IncomeOrExpense(BaseModel):
    description: str
    amount: float


class RemoveItem(BaseModel):
    index_or_description: int | str
