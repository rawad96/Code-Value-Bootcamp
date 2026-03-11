from solution.models.category import Category, CategoryType
from solution.services.category_service import CategoryService
from unittest.mock import Mock
from uuid import uuid4


def test_create_category():
    mock_repo = Mock()
    service = CategoryService(
        repo=mock_repo,
    )

    category = Category(id=str(uuid4()), name="Salary", type=CategoryType.INCOME)
    result = service.creat_category(category)

    mock_repo.create.assert_called_once()
    assert result == {"Message": "Category created"}


def test_get_all_categories():
    mock_repo = Mock()
    service = CategoryService(
        repo=mock_repo,
    )

    categories = [
        Category(id=str(uuid4()), name="Salary", type=CategoryType.INCOME),
        Category(id=str(uuid4()), name="Food", type=CategoryType.EXPENSE),
    ]
    mock_repo.get_all.return_value = categories

    result = service.get_all_categories()

    mock_repo.get_all.assert_called_once()
    assert result == categories


def test_get_by_id():
    mock_repo = Mock()
    service = CategoryService(
        repo=mock_repo,
    )

    category_id = str(uuid4())
    category = Category(id=category_id, name="Salary", type=CategoryType.INCOME)
    mock_repo.get.return_value = category

    result = service.get_by_id(category_id)

    mock_repo.get.assert_called_once_with(category_id)
    assert result == category


def test_update_category():
    mock_repo = Mock()
    service = CategoryService(
        repo=mock_repo,
    )

    category_id = str(uuid4())
    category = Category(id=category_id, name="Salary", type=CategoryType.INCOME)
    mock_repo.update.return_value = category

    result = service.update_category(category)

    mock_repo.update.assert_called_once_with(category)
    assert result == category


def test_delete_category():
    mock_repo = Mock()
    service = CategoryService(
        repo=mock_repo,
    )

    category_id = str(uuid4())
    result = service.delete_category(category_id)

    mock_repo.delete.assert_called_once_with(category_id)
    assert result == {"Message": "Category deleted"}
