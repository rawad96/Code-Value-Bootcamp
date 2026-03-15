import pytest
from typing import Any
from unittest.mock import AsyncMock, Mock

from solution.services.account_service import AccountService
from solution.services.transaction_service import TransactionService
from solution.services.category_service import CategoryService
from solution.services.transfer_service import TransferService
from solution.services.reports_service import ReportsService


class AsyncContextManager:
    """Async context manager that yields the given object (mimics session_maker() / session.begin())."""

    def __init__(self, obj: Any) -> None:
        self.obj = obj

    async def __aenter__(self) -> Any:
        return self.obj

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """"""


@pytest.fixture
def mock_session() -> AsyncMock:
    """Mock AsyncSession; .begin() returns async context manager per exercise 9."""
    session = AsyncMock()
    session.begin = Mock(return_value=AsyncContextManager(session))
    return session


@pytest.fixture
def mock_session_maker(mock_session: AsyncMock) -> Mock:
    """Mock async_session_maker: callable returning async context manager that yields mock session (exercise 9)."""
    return Mock(return_value=AsyncContextManager(mock_session))


@pytest.fixture
def category_service(
    mock_session: AsyncMock, mock_session_maker: Mock
) -> CategoryService:
    repo = AsyncMock()
    service = CategoryService(repo=repo, session_maker=mock_session_maker)
    return service


@pytest.fixture
def account_service(
    category_service: CategoryService, mock_session: AsyncMock, mock_session_maker: Mock
) -> AccountService:
    """AccountService with mock repo and mock session_maker (exercise 9: Async mocks for repo, session_maker)."""
    repo = AsyncMock()
    transaction_service = AsyncMock()
    service = AccountService(
        repo=repo,
        transaction_service=transaction_service,
        category_service=category_service,
        session_maker=mock_session_maker,
    )
    return service


@pytest.fixture
def transaction_service(
    mock_session_maker: Mock,
) -> TransactionService:
    repo = AsyncMock()
    service = TransactionService(
        repo=repo,
        session_maker=mock_session_maker,
    )
    return service


@pytest.fixture
def transfer_service(
    transaction_service: TransactionService,
    category_service: CategoryService,
    mock_session_maker: Mock,
) -> TransferService:
    repo = AsyncMock()
    service = TransferService(
        repo=repo,
        transaction_service=transaction_service,
        category_service=category_service,
        session_maker=mock_session_maker,
    )
    return service


@pytest.fixture
def reports_service(
    category_service: CategoryService,
    account_service: AccountService,
    transaction_service: TransactionService,
) -> ReportsService:
    service = ReportsService(
        category_service=category_service,
        account_service=account_service,
        transaction_service=transaction_service,
    )
    return service
