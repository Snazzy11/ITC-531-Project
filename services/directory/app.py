import math
import os
import socket
from datetime import datetime, timezone

from fastapi import FastAPI, Path, status
from pydantic import BaseModel, Field

APP_NAME = os.getenv("APP_NAME", "Club Directory Service")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# The directory shows 10 clubs per page, so 25 clubs need 3 pages to list them all.
CLUBS_PER_PAGE = 10

app = FastAPI(title=APP_NAME, version=APP_VERSION)


class Health(BaseModel):
    status: str
    timestamp: str
    hostname: str
    environment: str


class EchoRequest(BaseModel):
    message: str


class Order(BaseModel):
    club_id: int = Field(gt=0)
    student_name: str = Field(min_length=2)
    student_email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.get("/")
async def root():
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname(),
        "docs": "/docs",
    }


@app.get("/health", response_model=Health)
async def health():
    return Health(
        status="healthy",
        timestamp=datetime.now(timezone.utc).isoformat(),
        hostname=socket.gethostname(),
        environment=ENVIRONMENT,
    )


@app.post("/echo")
async def echo(payload: EchoRequest):
    return {"you_sent": payload.message, "length": len(payload.message)}


@app.get("/compute/{n}")
async def compute(n: int = Path(ge=0)):
    return {"clubs": n, "per_page": CLUBS_PER_PAGE, "pages": math.ceil(n / CLUBS_PER_PAGE)}


@app.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(payload: Order):
    return {"status": "received", **payload.model_dump()}


@app.get("/directory/status")
async def directory_status():
    return {
        "service": "directory",
        "status": "ok",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname(),
    }
