import json

FILE_NAME = "./jsons/company.json"
READ_MODE = "r"

DEPARTMENTS = "departments"
TEAMS = "teams"
EMPLOYEES = "employees"
NAME = "name"


def get_all_employee_names(company: dict) -> list[str]:
    all_teams = [
        team for department in company[DEPARTMENTS] for team in department[TEAMS]
    ]
    return [employee[NAME] for team in all_teams for employee in team[EMPLOYEES]]


def get_employees_by_department(company: dict, department: str) -> list[str]:
    for dept in company[DEPARTMENTS]:
        if dept[NAME] == department:
            return [
                employee[NAME] for team in dept[TEAMS] for employee in team[EMPLOYEES]
            ]
    return []


def get_average_salary(teams: dict) -> float:
    salaries = [employee["salary"] for team in teams for employee in team[EMPLOYEES]]
    return round(sum(salaries) / len(salaries) if salaries else 0, 2)


def get_average_salary_by_department(
    company: dict,
) -> dict[str, float]:
    return {
        dept[NAME]: get_average_salary(dept[TEAMS]) for dept in company[DEPARTMENTS]
    }


def extract_high_earners(teams: dict, threshold: int) -> list[str]:
    return [
        employee[NAME]
        for team in teams
        for employee in team[EMPLOYEES]
        if employee["salary"] > threshold
    ]


def get_high_earners(company: dict, threshold: int) -> dict[str, list[str]]:
    return {
        department[NAME]: extract_high_earners(department[TEAMS], threshold=threshold)
        for department in company[DEPARTMENTS]
    }


THRESHOLD = 100000

if __name__ == "__main__":
    with open(FILE_NAME, READ_MODE) as file:
        data_dict = json.load(file)

    # print(get_all_employee_names(company=data_dict))
    # print(get_employees_by_department(company=data_dict, department="Engineering"))
    # print(get_average_salary_by_department(company=data_dict))
    print(get_high_earners(company=data_dict, threshold=THRESHOLD))
