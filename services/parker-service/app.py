import os
import socket
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

APP_NAME = os.getenv("APP_NAME", "ITC 532 Module 1 Service")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI(title=APP_NAME, version=APP_VERSION)


class Health(BaseModel):
    status: str
    timestamp: str
    hostname: str
    environment: str


class EchoRequest(BaseModel):
    message: str


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
