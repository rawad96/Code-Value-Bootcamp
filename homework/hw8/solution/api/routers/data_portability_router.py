from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from solution.services.import_export_service import DataPortabilityService


router = APIRouter(prefix="/data", tags=["Data"])

service = DataPortabilityService()


@router.get("/export")
def export_data() -> FileResponse:
    """Returns zip file with all data."""
    file_path = service.export_data()

    return FileResponse(file_path, filename="backup.zip")


@router.post("/import")
def import_data(file: UploadFile = File(...)) -> dict[str, str]:
    """Imports data from uploaded zip."""
    path = f"temp_{file.filename}"

    with open(path, "wb") as fi:
        fi.write(file.file.read())

    service.import_data(path)

    return {"message": "Import successful"}
