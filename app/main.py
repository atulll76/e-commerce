from fastapi import FastAPI
from app.routers.verification import router as verification_router
from app.routers.users import router as users_router
from app.routers.products import router as products_router
from app.routers.orders import router as orders_router

app = FastAPI(
    title="E-Commerce API Backend",
    description="Backend service demonstrating Async Repository Layer pattern for MySQL",
    version="1.0.0",
)

app.include_router(verification_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Repository Layer validation service is active.",
    }
