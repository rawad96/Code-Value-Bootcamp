from solution.employee import Employee
from solution.full_timer_employee import FullTimer
from solution.manager_employee import Manager

HOURLY_RATE = 25.0
BOB_ANNUAL_SALARY = 90000
CAROL_ANNUAL_SALARY = 150000

NUMBER_OF_MONTHS = 12
HOURS_PER_MONTH = 160

MANAGER_BONUS = 0.15

ENGENEERING_DEPARTMENT = "Engineering"


def test_employee_wage_calculation() -> None:
    emp = Employee("E001", "Alice Johnson", HOURLY_RATE)
    assert emp.get_wage() == HOURLY_RATE * HOURS_PER_MONTH


def test_full_timer_wage_calculation() -> None:
    full_timer = FullTimer(
        "E002", "Bob Smith", BOB_ANNUAL_SALARY, ENGENEERING_DEPARTMENT
    )
    assert full_timer.get_wage() == BOB_ANNUAL_SALARY / NUMBER_OF_MONTHS


def test_manager_wage_calculation() -> None:
    manager = Manager(
        "E003",
        "Carol White",
        CAROL_ANNUAL_SALARY,
        ENGENEERING_DEPARTMENT,
        8,
        MANAGER_BONUS,
    )
    expected_wage = (CAROL_ANNUAL_SALARY / NUMBER_OF_MONTHS) * (1 + MANAGER_BONUS)
    assert manager.get_wage() == expected_wage


def test_polymorphism_in_employee_collection() -> None:
    contractor = Employee("E001", "Alice Johnson", HOURLY_RATE)
    full_timer = FullTimer(
        "E002", "Bob Smith", BOB_ANNUAL_SALARY, ENGENEERING_DEPARTMENT
    )
    manager = Manager(
        "E003",
        "Carol White",
        CAROL_ANNUAL_SALARY,
        ENGENEERING_DEPARTMENT,
        8,
        MANAGER_BONUS,
    )

    employees = [contractor, full_timer, manager]
    total_monthly_payroll = sum(emp.get_wage() for emp in employees)
    expected_total = (
        (HOURLY_RATE * HOURS_PER_MONTH)
        + (BOB_ANNUAL_SALARY / NUMBER_OF_MONTHS)
        + ((CAROL_ANNUAL_SALARY / NUMBER_OF_MONTHS) * (1 + MANAGER_BONUS))
    )
    assert total_monthly_payroll == expected_total


def test_employee_info_display() -> None:
    emp = Employee("E001", "Alice Johnson", HOURLY_RATE)
    full_timer = FullTimer(
        "E002", "Bob Smith", BOB_ANNUAL_SALARY, ENGENEERING_DEPARTMENT
    )
    manager = Manager(
        "E003",
        "Carol White",
        CAROL_ANNUAL_SALARY,
        ENGENEERING_DEPARTMENT,
        8,
        MANAGER_BONUS,
    )
    expected_contractor_info = """Employee E001:
Alice Johnson
Hourly Rate: $25.00
Per Month: $4000.00"""

    expected_full_timer_info = """Full-Time Employee E002:
Bob Smith
Department: Engineering
Per Month: $7500.00
Salary: $90000/year"""

    expected_manager_info = """Manager E003:
Carol White
Department: Engineering
Team Size: 8
Per Month: $14375.00
Salary: $150000/year
Bonus: 15.0%"""

    assert emp.get_info() == expected_contractor_info

    assert full_timer.get_info() == expected_full_timer_info

    assert manager.get_info() == expected_manager_info
