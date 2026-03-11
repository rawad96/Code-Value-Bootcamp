import uvicorn

from solution.api.routers.app import app

PORT = 8000

uvicorn.run(
    app,
    host="127.0.0.1",
    port=PORT,
)
