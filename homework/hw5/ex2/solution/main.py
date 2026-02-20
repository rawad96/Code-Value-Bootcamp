from employee import Employee
from full_timer_employee import FullTimer
from manager_employee import Manager


if __name__ == "__main__":
    # employee = Employee("E001", "Alice", 15.0)
    full_timer = FullTimer("E002", "Bob", 60000, "Engineering")
    # manager = Manager("E003", "Charlie", 80000, "Sales", 5, 0.1)

    # print(employee.get_info())
    print(full_timer.get_info())
    # print(manager.get_info())
