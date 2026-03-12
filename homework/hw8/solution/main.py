import uvicorn

from solution.api.routers.app import app
from seed.seed_default_categories import seed_categories

seed_categories()

PORT = 8000

uvicorn.run(
    app,
    host="127.0.0.1",
    port=PORT,
)
