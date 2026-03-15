import pytest
from solution.models.category import CategoryType
from solution.services.category_service import CategoryService
from unittest.mock import Mock
from uuid import uuid4

from constants.headers import TablesHeaders


@pytest.mark.asyncio
async def test_creat_category(category_service: CategoryService) -> None:
    created_id = uuid4()

    test_data = {
        TablesHeaders.NAME.value: "Food",
        TablesHeaders.TYPE.value: CategoryType.EXPENSE.value,
    }

    mock_category = Mock()
    mock_category.id = created_id
    mock_category.name = test_data[TablesHeaders.NAME.value]
    mock_category.type = CategoryType(test_data[TablesHeaders.TYPE.value])

    category_service.repo.create.return_value = mock_category

    result = await category_service.creat_category(test_data)

    session = category_service.session_maker.return_value.obj

    session.begin.assert_called_once()
    category_service.session_maker.assert_called_once()
    category_service.repo.create.assert_awaited_once()

    new_category, session_passed = category_service.repo.create.call_args[0]

    assert new_category.name == test_data[TablesHeaders.NAME.value]
    assert new_category.type == CategoryType(test_data[TablesHeaders.TYPE.value])
    assert session_passed is session

    assert result[TablesHeaders.NAME.value] == test_data[TablesHeaders.NAME.value]


@pytest.mark.asyncio
async def test_get_all_categories(category_service: CategoryService) -> None:
    first_cat = {"name": "Food", "type": CategoryType.EXPENSE.value}
    second_cat = {"name": "Salary", "type": CategoryType.INCOME.value}

    cat1 = Mock()
    cat1.id = uuid4()
    cat1.name = first_cat[TablesHeaders.NAME.value]
    cat1.type = CategoryType(first_cat[TablesHeaders.TYPE.value])

    cat2 = Mock()
    cat2.id = uuid4()
    cat2.name = second_cat[TablesHeaders.NAME.value]
    cat2.type = CategoryType(second_cat[TablesHeaders.TYPE.value])

    category_service.repo.get_all.return_value = [cat1, cat2]

    result = await category_service.get_all_categories()

    session = category_service.session_maker.return_value.obj

    category_service.session_maker.assert_called_once()
    category_service.repo.get_all.assert_awaited_once_with(session)

    assert len(result) == 2
    assert result[0][TablesHeaders.NAME.value] == cat1.name
    assert result[1][TablesHeaders.NAME.value] == cat2.name


@pytest.mark.asyncio
async def test_get_by_id(category_service: CategoryService) -> None:
    category_id = uuid4()

    mock_category = Mock()
    mock_category.id = category_id
    mock_category.name = "Food"
    mock_category.type = CategoryType.EXPENSE

    category_service.repo.get.return_value = mock_category

    result = await category_service.get_by_id(category_id)

    session = category_service.session_maker.return_value.obj

    category_service.session_maker.assert_called_once()
    category_service.repo.get.assert_awaited_once_with(str(category_id), session)

    assert result[TablesHeaders.NAME.value] == "Food"


@pytest.mark.asyncio
async def test_get_by_id_not_found(category_service: CategoryService) -> None:
    category_id = uuid4()
    category_service.repo.get.return_value = None
    result = await category_service.get_by_id(category_id)

    assert result is None


@pytest.mark.asyncio
async def test_get_by_name(category_service: CategoryService) -> None:
    mock_category = Mock()
    mock_category.id = uuid4()
    mock_category.name = "Food"
    mock_category.type = CategoryType.EXPENSE

    category_service.repo.get_all.return_value = [mock_category]

    result = await category_service.get_by_name("Food")

    session = category_service.session_maker.return_value.obj

    category_service.repo.get_all.assert_awaited_once_with(session)

    assert result[TablesHeaders.NAME.value] == "Food"


@pytest.mark.asyncio
async def test_get_by_name_not_found(category_service: CategoryService) -> None:
    category_service.repo.get_all.return_value = []

    result = await category_service.get_by_name("Food")

    assert result is None


@pytest.mark.asyncio
async def test_update_category(category_service: CategoryService) -> None:
    category_id = uuid4()

    test_data = {
        TablesHeaders.ID.value: category_id,
        TablesHeaders.NAME.value: "Updated",
        TablesHeaders.TYPE.value: CategoryType.INCOME.value,
    }

    mock_category = Mock()
    mock_category.id = category_id
    mock_category.name = test_data[TablesHeaders.NAME.value]
    mock_category.type = CategoryType(test_data[TablesHeaders.TYPE.value])

    category_service.repo.update.return_value = mock_category

    result = await category_service.update_category(test_data)

    session = category_service.session_maker.return_value.obj

    category_service.repo.update.assert_awaited_once()

    new_category, session_passed = category_service.repo.update.call_args[0]

    assert new_category.name == test_data[TablesHeaders.NAME.value]
    assert new_category.type == CategoryType(test_data[TablesHeaders.TYPE.value])
    assert session_passed is session

    assert result[TablesHeaders.NAME.value] == test_data[TablesHeaders.NAME.value]


@pytest.mark.asyncio
async def test_delete_category(category_service: CategoryService) -> None:
    category_id = uuid4()
    result = await category_service.delete_category(category_id)
    session = category_service.session_maker.return_value.obj
    category_service.repo.delete.assert_awaited_once_with(str(category_id), session)

    assert result == {"Message": "Category deleted"}


@pytest.mark.asyncio
async def test_get_by_ids(category_service: CategoryService) -> None:
    category = Mock()
    category.id = uuid4()

    mock_result = Mock()
    mock_scalars = Mock()
    mock_scalars.all.return_value = [category]
    mock_result.scalars.return_value = mock_scalars

    session = category_service.session_maker.return_value.obj
    session.execute.return_value = mock_result

    ids = [str(category.id)]

    result = await category_service.get_by_ids(ids, session)

    assert result == [category]
