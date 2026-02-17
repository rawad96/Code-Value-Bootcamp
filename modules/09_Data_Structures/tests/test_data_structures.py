from solution.data_structures import (
    get_all_employee_names,
    get_employees_by_department,
    get_average_salary_by_department,
    get_high_earners,
)
import pytest


@pytest.fixture
def company_data():
    return {
        "departments": [
            {
                "name": "Engineering",
                "teams": [
                    {
                        "name": "Backend",
                        "employees": [
                            {"name": "Alice", "salary": 120000},
                            {"name": "Bob", "salary": 110000},
                        ],
                    },
                    {
                        "name": "Frontend",
                        "employees": [{"name": "Charlie", "salary": 105000}],
                    },
                ],
            },
            {
                "name": "Sales",
                "teams": [
                    {
                        "name": "Direct Sales",
                        "employees": [
                            {"name": "Diana", "salary": 95000},
                            {"name": "Eve", "salary": 98000},
                        ],
                    }
                ],
            },
        ]
    }


def test_get_all_employee_names(company_data):
    expected = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    assert get_all_employee_names(company_data) == expected


def test_get_employees_by_department(company_data):
    expected_engineering = ["Alice", "Bob", "Charlie"]
    expected_sales = ["Diana", "Eve"]
    assert (
        get_employees_by_department(company_data, "Engineering") == expected_engineering
    )
    assert get_employees_by_department(company_data, "Sales") == expected_sales


def test_get_average_salary_by_department(company_data):
    expected = {
        "Engineering": 111666.67,
        "Sales": 96500.00,
    }
    assert get_average_salary_by_department(company_data) == expected


def test_get_high_earners(company_data):
    threshold = 100000
    expected = {"Engineering": ["Alice", "Bob", "Charlie"], "Sales": []}
    assert get_high_earners(company_data, threshold) == expected
