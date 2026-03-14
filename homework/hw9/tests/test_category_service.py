import pytest
from solution.models.category import Category, CategoryType
from solution.services.category_service import CategoryService
from unittest.mock import Mock
from uuid import uuid4
from typing import Any


@pytest.fixture
def mock_repo() -> Mock:
    """Returns mock repo."""
    return Mock()


@pytest.fixture
def category_service(mock_repo: Mock) -> CategoryService:
    """Returns CategoryService with mock repo."""
    return CategoryService(repo=mock_repo)


def test_create_category(category_service: CategoryService, mock_repo: Mock) -> None:
    """Checks creat_category calls repo.create and returns message."""
    category_data: dict[str, Any] = {"name": "Salary", "type": CategoryType.INCOME}
    result = category_service.creat_category(category_data)

    mock_repo.create.assert_called_once()
    created_category = mock_repo.create.call_args[0][0]
    assert created_category.name == "Salary"
    assert created_category.type == CategoryType.INCOME
    assert created_category.is_deleted == "false"
    assert result == {"Message": "Category created"}


def test_get_all_categories(category_service: CategoryService, mock_repo: Mock) -> None:
    categories = [
        Category(
            id=str(uuid4()),
            name="Salary",
            type=CategoryType.INCOME,
            is_deleted="false",
        ),
        Category(
            id=str(uuid4()), name="Food", type=CategoryType.EXPENSE, is_deleted="false"
        ),
    ]
    mock_repo.get_all.return_value = categories

    result = category_service.get_all_categories()

    mock_repo.get_all.assert_called_once()
    assert result == [
        {
            "id": str(categories[0].id),
            "name": "Salary",
            "type": "income",
            "is_deleted": "false",
        },
        {
            "id": str(categories[1].id),
            "name": "Food",
            "type": "expense",
            "is_deleted": "false",
        },
    ]


def test_get_by_id(category_service: CategoryService, mock_repo: Mock) -> None:
    """Checks get_by_id returns category dict."""
    category_id = str(uuid4())
    category = Category(
        id=category_id, name="Salary", type=CategoryType.INCOME, is_deleted="false"
    )
    mock_repo.get.return_value = category

    result = category_service.get_by_id(category_id)

    mock_repo.get.assert_called_once_with(category_id)
    assert result == {
        "id": category_id,
        "name": "Salary",
        "type": "income",
        "is_deleted": "false",
    }


def test_get_by_name(category_service: CategoryService, mock_repo: Mock) -> None:
    cat1 = Category(
        id=str(uuid4()), name="Salary", type=CategoryType.INCOME, is_deleted="false"
    )
    cat2 = Category(
        id=str(uuid4()), name="Food", type=CategoryType.EXPENSE, is_deleted="false"
    )
    mock_repo.get_all.return_value = [cat1, cat2]

    result = category_service.get_by_name("Food")
    assert result == {
        "id": str(cat2.id),
        "name": "Food",
        "type": "expense",
        "is_deleted": "false",
    }

    result_none = category_service.get_by_name("Unknown")
    assert result_none is None


def test_update_category(category_service: CategoryService, mock_repo: Mock) -> None:
    """Checks update_category calls repo.update and returns dict."""
    category_id = str(uuid4())
    category_data: dict[str, Any] = {
        "id": category_id,
        "name": "Salary",
        "type": CategoryType.INCOME,
    }
    updated_category = Category(
        id=category_id, name="Salary", type=CategoryType.INCOME, is_deleted="false"
    )
    mock_repo.update.return_value = updated_category

    result = category_service.update_category(category_data)

    mock_repo.update.assert_called_once()
    updated_call_arg = mock_repo.update.call_args[0][0]
    assert updated_call_arg.is_deleted == "false"
    assert result == {
        "id": category_id,
        "name": "Salary",
        "type": "income",
        "is_deleted": "false",
    }


def test_delete_category(category_service: CategoryService, mock_repo: Mock) -> None:
    """Checks delete_category calls repo.delete and returns message."""
    category_id = str(uuid4())
    result = category_service.delete_category(category_id)

    mock_repo.delete.assert_called_once_with(category_id)
    assert result == {"Message": "Category deleted"}
