from solution.services.account_service import AccountService

from constants.headers import account_headers_request

from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from decimal import Decimal
from typing import Any

router = APIRouter(prefix="/accounts", tags=["Accounts"])

service = AccountService()

IVALID_UUID_FORMAT = "Invalid UUID format"
ACCOUNT_NOT_FOUND = "Account not found"


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_account(account: dict[str, Any]) -> dict[str, Any]:
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
    return await service.create_account(account)


@router.get("/")
async def get_accounts() -> list[dict[str, Any]]:
    """Returns all accounts."""
    return await service.get_all_accounts()


@router.get("/{account_id}")
async def get_account(account_id: str) -> dict[str, Any]:
    try:
        account = await service.get_by_id(UUID(account_id))
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
async def update_account(account: dict[str, Any]) -> dict[str, Any]:
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

    updated_account = await service.update_account(account)
    if updated_account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ACCOUNT_NOT_FOUND
        )
    return updated_account


@router.delete("/{account_id}")
async def delete_account(account_id: str) -> dict[str, str]:
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=IVALID_UUID_FORMAT
        )

    account = await service.get_by_id(id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ACCOUNT_NOT_FOUND
        )
    return await service.delete_account(id)


@router.get("/{account_id}/balance")
async def calculate_balance(account_id: str) -> Decimal:
    """Returns balance for account."""
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=IVALID_UUID_FORMAT
        )

    account = await service.get_by_id(id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ACCOUNT_NOT_FOUND
        )
    return await service.calculate_balance(id)


@router.get("/get/net/worth")
async def calculate_net_worth() -> Decimal:
    """Returns net worth of all accounts."""
    return await service.calculate_net_worth()
