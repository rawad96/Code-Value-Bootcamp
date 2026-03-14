from fastapi import FastAPI

from solution.api.routers.account_router import router as account_router
from solution.api.routers.category_router import router as category_router
from solution.api.routers.transaction_router import router as transaction_router
from solution.api.routers.transfer_router import router as transfer_router
from solution.api.routers.reports_router import router as report_router
from solution.api.routers.data_portability_router import router as data_router

app = FastAPI()

app.include_router(account_router)
app.include_router(category_router)
app.include_router(transaction_router)
app.include_router(transfer_router)
app.include_router(report_router)
app.include_router(data_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "OK"}
