from .employee import Employee

NUMBER_OF_MONTHS = 12


class FullTimer(Employee):
    def __init__(self, id: str, name: str, annual_salary: int, department: str):
        super().__init__(id, name, 0)
        self.annual_salary = annual_salary
        self.department = department

    def get_wage(self) -> float:
        """returns wage per month"""
        return self.annual_salary / NUMBER_OF_MONTHS

    def get_info(self) -> str:
        return f"""Full-Time Employee {self.id}:
{self.name}
Department: {self.department}
Per Month: ${self.get_wage():.2f}
Salary: ${self.annual_salary}/year"""
