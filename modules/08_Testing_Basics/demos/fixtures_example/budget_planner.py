
from dataclasses import dataclass


@dataclass
class Income:
    id: int
    amount: float
    category: str


class BudgetPlanner:

    def __init__(self):
        self.balance = 0
        self.incomes = []

    def add_income(self, amount: float, category: str):
        raise NotImplementedError("Not implemented yet")
    
    def get_balance(self) -> float:
        raise NotImplementedError("Not implemented yet")
    
    def number_of_incomes(self) -> int:
        raise NotImplementedError("Not implemented yet")
    
    def average_income_amount(self) -> float:
        raise NotImplementedError("Not implemented yet")