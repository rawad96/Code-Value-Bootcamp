from employee import Employee


class FullTimer(Employee):
    def __init__(self, id: str, name: str, annual_salary: int, department: str):
        super().__init__(id, name, 0)
        self.annual_salary = annual_salary
        self.department = department

    def get_wage(self) -> float:
        """returns wage per month"""
        return self.annual_salary / 12

    def get_info(self) -> str:
        return f"""ID: {self.id}
Name: {self.name}
Department: {self.department}
Per Month Wage: {self.get_wage()}$"""
