from fastapi import FastAPI, Request
import time
from .database import Base, engine
from .routes import router
from .logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(router)


@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(f"{request.method} {request.url} completed in {duration:.4f}s")

    return response