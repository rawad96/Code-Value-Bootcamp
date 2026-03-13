from solution.services.category_service import CategoryService

from constants.headers import category_headers_request

from fastapi import APIRouter, HTTPException, status, Body
from uuid import UUID
from typing import Any

router = APIRouter(prefix="/categories", tags=["Categories"])

service = CategoryService()

IVALID_UUID_FORMAT = "Invalid UUID format"
CATEGORY_NOT_FOUND = "Category not found"


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_category(category: dict[str, Any] = Body(...)) -> dict[str, str]:
    for field in category_headers_request:
        if field not in category:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail=f"Missing '{field}'",
            )
    if category["type"] not in ["income", "expense"]:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Type must be 'income' or 'expense'",
        )
    return service.creat_category(category)


@router.get("/")
def get_all_categories() -> list[dict[str, Any]]:
    return service.get_all_categories()


@router.get("/{category_id}")
def get_category(category_id: str) -> dict[str, Any]:
    try:
        category = service.get_by_id(UUID(category_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=IVALID_UUID_FORMAT,
        )
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=CATEGORY_NOT_FOUND
        )
    return category


@router.get("/by-name/{name}")
def get_category_by_name(name: str) -> dict[str, Any]:
    category = service.get_by_name(name)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=CATEGORY_NOT_FOUND
        )
    return category


@router.put("/")
def update_category(category: dict[str, Any] = Body(...)) -> dict[str, Any]:
    if "id" not in category:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Category must have 'id'",
        )
    try:
        category["id"] = UUID(category["id"])
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=IVALID_UUID_FORMAT
        )

    updated_category = service.update_category(category)
    if updated_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=CATEGORY_NOT_FOUND
        )
    return updated_category


@router.delete("/{category_id}")
def delete_category(category_id: str) -> dict[str, str]:
    try:
        service.delete_category(UUID(category_id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=IVALID_UUID_FORMAT,
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=CATEGORY_NOT_FOUND
        )
    return {"Message": "Category deleted"}
