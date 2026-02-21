from .full_timer_employee import FullTimer

NUMBER_OF_MONTHS = 12


class Manager(FullTimer):
    def __init__(
        self,
        id: str,
        name: str,
        annual_salary: int,
        department: str,
        reports: int,
        bonus: float,
    ):
        super().__init__(id, name, annual_salary, department)
        self.reports = reports
        if not 0 <= bonus <= 1:
            raise ValueError("Bonus must be between 0 and 1")
        self.bonus = bonus

    def get_wage(self) -> float:
        """returns wage per month"""
        return (self.annual_salary / NUMBER_OF_MONTHS) * (1 + self.bonus)

    def get_info(self) -> str:
        return f"""Manager {self.id}:
{self.name}
Department: {self.department}
Team Size: {self.reports}
Per Month: ${self.get_wage():.2f}
Salary: ${self.annual_salary}/year
Bonus: {self.bonus * 100}%"""
