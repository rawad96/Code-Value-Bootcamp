from solution.services.transaction_service import TransactionService

from constants.headers import transaction_headers_request

from fastapi import APIRouter, HTTPException, status, Body
from uuid import UUID
from typing import Any

IVALID_UUID_FORMAT = "Invalid UUID format"
TRANSACTION_NOT_FOUND = "Transaction not found"


router = APIRouter(prefix="/transactions", tags=["Transactions"])

service = TransactionService()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: dict[str, Any] = Body(...)) -> dict[str, str]:
    """Creates transaction."""
    for field in transaction_headers_request:
        if field not in transaction:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail=f"Missing '{field}'",
            )
    try:
        transaction["account_id"] = UUID(transaction["account_id"])
        transaction["category_id"] = UUID(transaction["category_id"])
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    return service.creat_trnsaction(transaction)


@router.get("/")
def get_all_transactions() -> list[dict[str, Any]]:
    """Returns all transactions."""
    return service.get_all_transaction()


@router.get("/{transaction_id}")
def get_transaction(transaction_id: str) -> dict[str, Any]:
    """Returns transaction by id."""
    try:
        transaction = service.get_by_id(UUID(transaction_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=TRANSACTION_NOT_FOUND,
        )

    return transaction


@router.get("/account/{account_id}")
def get_transactions_by_account(account_id: str) -> list[dict[str, Any]]:
    """Returns all transactions for account."""
    try:
        transactions = service.get_all_by_account(UUID(account_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    return transactions


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: str) -> dict[str, str]:
    """Deletes transaction."""
    try:
        transaction = service.get_by_id(UUID(transaction_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=TRANSACTION_NOT_FOUND,
        )

    return service.delete_transaction(UUID(transaction_id))
