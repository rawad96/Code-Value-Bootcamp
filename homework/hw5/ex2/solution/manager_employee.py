from full_timer_employee import FullTimer


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
        super().__init__(self, id, name, annual_salary, department)
        self.reports = reports
        if not 0 <= bonus <= 1:
            raise ValueError("Bonus must be between 0 and 1")
        self.bonus = bonus

    def get_wage(self) -> float:
        """returns wage per month"""
        return (self.annual_salary / 12) * (1 + self.bonus)

    def get_info(self) -> str:
        return f"""ID: {self.id}
Name: {self.name}
Department: {self.department}
Number of Reports: {self.reports}
Per Month Wage: {self.get_wage()}"""
