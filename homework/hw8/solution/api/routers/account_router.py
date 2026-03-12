from solution.services.account_service import AccountService

from constants.headers import account_headers_request

from fastapi import APIRouter, Body, HTTPException, status
from uuid import UUID
from decimal import Decimal
from typing import Any

router = APIRouter(prefix="/accounts", tags=["Accounts"])

service = AccountService()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_account(account: dict[str, Any] = Body(...)) -> dict[str, str]:
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
    return service.get_all_accounts()


@router.get("/{account_id}")
def get_account(account_id: str) -> dict[str, Any]:
    try:
        account = service.get_by_id(UUID(account_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UUID format"
        )

    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )
    return account


@router.put("/")
def update_account(account: dict[str, Any]) -> dict[str, Any]:
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
