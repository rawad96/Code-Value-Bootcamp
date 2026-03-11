from solution.services.account_service import AccountService
from solution.models.account import Account


from fastapi import APIRouter, Body, HTTPException, status
from uuid import UUID
from decimal import Decimal
from typing import Any

router = APIRouter(prefix="/accounts", tags=["Accounts"])

service = AccountService()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_account(account: dict[str, Any] = Body(...)) -> dict[str, str]:
    if "name" not in account or "opening_balance" not in account:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Missing 'name' or 'opening_balance'.",
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
def get_accounts() -> list[Account]:
    return service.get_all_accounts()


@router.get("/{account_id}")
def get_account(account_id: str) -> Account:
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UUID format"
        )

    account = service.get_by_id(UUID(id))
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )
    return account


@router.put("/")
def update_account(account: dict[str, Any]) -> Account:
    if "id" not in account:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Missing 'id'"
        )

    try:
        account["id"] = UUID(account["id"])
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UUID format"
        )
    updated_account = service.update_account(account)
    if updated_account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )
    return updated_account


@router.delete("/{account_id}")
def delete_account(account_id: str) -> dict[str, str]:
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UUID format"
        )

    account = service.get_by_id(id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )
    return service.delete_account(id)


@router.get("/{account_id}/balance")
def calculate_balance(account_id: str) -> Decimal:
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UUID format"
        )

    account = service.get_by_id(id)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )
    return service.calculate_balance(id)


@router.get("/get/net/worth")
def calculate_net_worth() -> Decimal:
    return service.calculate_net_worth()
