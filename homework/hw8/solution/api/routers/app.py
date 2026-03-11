from fastapi import FastAPI

from solution.api.routers.account_router import router as account_router

app = FastAPI()

app.include_router(account_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "OK"}
