from employee import Employee
from full_timer_employee import FullTimer
from manager_employee import Manager

HOURLY_RATE = 25.0

if __name__ == "__main__":
    contractor = Employee("E001", "Alice Johnson", HOURLY_RATE)
    # full_timer = FullTimer("E002", "Bob Smith", 90000, "Engineering")
    # manager = Manager("E003", "Carol White", 150000, "Engineering", 8, 0.15)

    print(contractor.get_info())
    # print(full_timer.get_info())
    # print(manager.get_info())

    # employees = [contractor, full_timer, manager]
    # total_monthly_payroll = sum(emp.get_wage() for emp in employees)
    # formatted_total = f"${total_monthly_payroll:,.2f}"
    # print(f"Total monthly payroll: {formatted_total}")
