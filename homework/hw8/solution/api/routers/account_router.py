from solution.services.account_service import AccountService

from constants.headers import account_headers_request

from fastapi import APIRouter, Body, HTTPException, status
from uuid import UUID
from decimal import Decimal
from typing import Any

router = APIRouter(prefix="/accounts", tags=["Accounts"])

service = AccountService()

IVALID_UUID_FORMAT = "Invalid UUID format"
ACCOUNT_NOT_FOUND = "Account not found"


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_account(account: dict[str, Any] = Body(...)) -> dict[str, str]:
    """Creates account."""
    for field in account_headers_request:
        if field not in account:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail=f"Missing '{field}'",
            )
    try:
        account["opening_balance"] = Decimal(account["opening_balance"])
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="opening_balance must be a number",
        )
    return service.create_account(account)


@router.get("/")
def get_accounts() -> list[dict[str, Any]]:
    """Returns all accounts."""
    return service.get_all_accounts()


@router.get("/{account_id}")
def get_account(account_id: str) -> dict[str, Any]:
    try:
        account = service.get_by_id(UUID(account_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=IVALID_UUID_FORMAT
        )

    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ACCOUNT_NOT_FOUND
        )
    return account


@router.put("/")
def update_account(account: dict[str, Any]) -> dict[str, Any]:
    """Updates account."""
    if "id" not in account:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Missing 'id'"
        )

    try:
        account["id"] = UUID(account["id"])
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=IVALID_UUID_FORMAT
        )

    updated_account = service.update_account(account)
    if updated_account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ACCOUNT_NOT_FOUND
        )
    return updated_account


@router.delete("/{account_id}")
def delete_account(account_id: str) -> dict[str, str]:
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=IVALID_UUID_FORMAT
        )

    account = service.get_by_id(id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ACCOUNT_NOT_FOUND
        )
    return service.delete_account(id)


@router.get("/{account_id}/balance")
def calculate_balance(account_id: str) -> Decimal:
    """Returns balance for account."""
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=IVALID_UUID_FORMAT
        )

    account = service.get_by_id(id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ACCOUNT_NOT_FOUND
        )
    return service.calculate_balance(id)


@router.get("/get/net/worth")
def calculate_net_worth() -> Decimal:
    """Returns net worth of all accounts."""
    return service.calculate_net_worth()
