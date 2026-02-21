HOURS_PER_MONTH = 160


class Employee:
    def __init__(self, id: str, name: str, hourly_rate: float):
        self.id = id
        self.name = name
        self.hourly_rate = hourly_rate

    def get_wage(self) -> float:
        return self.hourly_rate * HOURS_PER_MONTH

    def get_info(self) -> str:
        return f"""Employee {self.id}:
{self.name}
Hourly Rate: ${self.hourly_rate:.2f}
Per Month: ${self.get_wage():.2f}"""
