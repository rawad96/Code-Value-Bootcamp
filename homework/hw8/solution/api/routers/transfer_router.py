from solution.services.transfer_service import TransferService

from constants.headers import transfer_headers_request

from fastapi import APIRouter, HTTPException, status, Body
from uuid import UUID
from typing import Any


router = APIRouter(prefix="/transfers", tags=["Transfers"])

service = TransferService()

IVALID_UUID_FORMAT = "Invalid UUID format"
TRANSFER_NOT_FOUND = "Transfer not found"


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_transfer(transfer: dict[str, Any] = Body(...)) -> dict[str, str]:

    for field in transfer_headers_request:
        if field not in transfer:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail=f"Missing '{field}'",
            )

    try:
        transfer["from_account_id"] = UUID(transfer["from_account_id"])
        transfer["to_account_id"] = UUID(transfer["to_account_id"])
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    if transfer["from_account_id"] == transfer["to_account_id"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot transfer to the same account",
        )

    return service.creat_transfer(transfer)


@router.get("/")
def get_all_transfers() -> list[dict[str, Any]]:
    return service.get_all_transfers()


@router.get("/{transfer_id}")
def get_transfer(transfer_id: str) -> dict[str, Any]:

    try:
        transfer = service.get_by_id(UUID(transfer_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    if transfer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=TRANSFER_NOT_FOUND,
        )

    return transfer


@router.get("/account/{account_id}")
def get_transfers_by_account(account_id: str) -> list[dict[str, Any]]:
    try:
        id = UUID(account_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    return service.get_all_by_account(id)


@router.delete("/{transfer_id}")
def delete_transfer(transfer_id: str) -> dict[str, str]:
    try:
        id = UUID(transfer_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )

    transfer = service.get_by_id(id)

    if transfer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=TRANSFER_NOT_FOUND,
        )

    return service.delete_transfer(id)
