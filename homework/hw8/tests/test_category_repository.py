import pytest
from unittest.mock import Mock
from uuid import uuid4
from solution.models.category import Category, CategoryType
from solution.repository.category_repository import CategoryRepository

from constants.headers import CSVHeaders

TRUE = "true"
FALSE = "false"


@pytest.fixture
def mock_accessor() -> Mock:
    """Returns mock accessor."""
    return Mock()


def test_create_category(mock_accessor: Mock) -> None:
    repo = CategoryRepository(accessor=mock_accessor)
    category_uuid = uuid4()

    category = Category(
        id=category_uuid,
        name="Test Category",
        type=CategoryType.EXPENSE,
        is_deleted=FALSE,
    )

    repo.create(category)

    mock_accessor.append_row.assert_called_once()
    args = mock_accessor.append_row.call_args[0][0]

    assert args[CSVHeaders.ID.value] == str(category_uuid)
    assert args[CSVHeaders.NAME.value] == "Test Category"
    assert args[CSVHeaders.TYPE.value] == str(CategoryType.EXPENSE.value)
    assert args[CSVHeaders.IS_DELETED.value] == FALSE


def test_get_category_by_id(mock_accessor: Mock) -> None:
    """Checks get returns category by id."""
    category_id = uuid4()
    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(category_id),
            CSVHeaders.NAME.value: "Test Category",
            CSVHeaders.TYPE.value: str(CategoryType.EXPENSE.value),
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = CategoryRepository(accessor=mock_accessor)
    returned_category = repo.get(category_id)

    assert isinstance(returned_category, Category)
    assert returned_category.id == category_id
    assert returned_category.name == "Test Category"


def test_get_all_categories(mock_accessor: Mock) -> None:
    """Checks get_all returns all non-deleted categories."""
    cat1_id = uuid4()
    cat2_id = uuid4()
    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(cat1_id),
            CSVHeaders.NAME.value: "Category 1",
            CSVHeaders.TYPE.value: str(CategoryType.EXPENSE.value),
            CSVHeaders.IS_DELETED.value: FALSE,
        },
        {
            CSVHeaders.ID.value: str(cat2_id),
            CSVHeaders.NAME.value: "Category 2",
            CSVHeaders.TYPE.value: str(CategoryType.INCOME.value),
            CSVHeaders.IS_DELETED.value: FALSE,
        },
    ]

    repo = CategoryRepository(accessor=mock_accessor)
    returned_categories = repo.get_all()

    assert len(returned_categories) == 2
    assert all(isinstance(cat, Category) for cat in returned_categories)


def test_update_category(mock_accessor: Mock) -> None:
    category_id = uuid4()
    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(category_id),
            CSVHeaders.NAME.value: "Old Name",
            CSVHeaders.TYPE.value: str(CategoryType.EXPENSE.value),
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = CategoryRepository(accessor=mock_accessor)

    updated_category = Category(
        id=category_id,
        name="New Name",
        type=CategoryType.EXPENSE,
        is_deleted=FALSE,
    )

    repo.update(updated_category)

    mock_accessor.write_all.assert_called_once()
    args = mock_accessor.write_all.call_args[0][0][0]
    assert args[CSVHeaders.NAME.value] == "New Name"


def test_delete_category(mock_accessor: Mock) -> None:
    """Checks delete marks row as deleted."""
    category_id = uuid4()
    mock_accessor.read_all.return_value = [
        {
            CSVHeaders.ID.value: str(category_id),
            CSVHeaders.NAME.value: "Category to Delete",
            CSVHeaders.TYPE.value: str(CategoryType.EXPENSE.value),
            CSVHeaders.IS_DELETED.value: FALSE,
        }
    ]

    repo = CategoryRepository(accessor=mock_accessor)
    repo.delete(category_id)

    mock_accessor.write_all.assert_called_once()
    args = mock_accessor.write_all.call_args[0][0][0]
    assert args[CSVHeaders.IS_DELETED.value] == TRUE
