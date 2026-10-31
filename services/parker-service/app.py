import os
import socket
import uuid
from datetime import datetime, timezone

from fastapi import FastAPI, Path, status
from pydantic import BaseModel, Field

APP_NAME = os.getenv("APP_NAME", "ITC 532 Module 1 Service")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# A 720p frame is 1280x720 pixels, and stored raw (no compression) each pixel takes 3 bytes, one each for red, green and blue.
FRAME_BYTES_720P = 1280 * 720 * 3

app = FastAPI(title=APP_NAME, version=APP_VERSION)


class Health(BaseModel):
    status: str
    timestamp: str
    hostname: str
    environment: str


class EchoRequest(BaseModel):
    message: str


class VideoOrder(BaseModel):
    title: str = Field(min_length=1)
    frames: int = Field(gt=0)
    fps: int = Field(ge=1, le=120)


def video_size(frames: int) -> dict:
    size_bytes = frames * FRAME_BYTES_720P
    return {"bytes": size_bytes, "megabytes": round(size_bytes / 1_000_000, 2)}


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
    return {"resolution": "1280x720", "frames": n, **video_size(n)}


@app.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: VideoOrder):
    return {
        "order_id": str(uuid.uuid4()),
        **order.model_dump(),
        "duration_seconds": round(order.frames / order.fps, 2),
        **video_size(order.frames),
    }
