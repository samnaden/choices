from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from logger import logger


class LogRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Response]
    ) -> Response:
        body = await request.body()

        logger.info(
            f"Incoming request: {request.method} {request.url.path} | Body: {body.decode(errors='ignore')}"
        )

        response = await call_next(request)

        return response
