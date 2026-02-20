class Employee:
    def __init__(self, id: str, name: str, hourly_rate: float):
        self.id = id
        self.name = name
        self.hourly_rate = hourly_rate

    def get_wage(self) -> float:
        return self.hourly_rate * 160

    def get_info(self) -> str:
        return f"""ID: {self.id}
Name: {self.name}
Hourly Rate: {self.hourly_rate}$
Per Month Wage: {self.get_wage()}$"""
