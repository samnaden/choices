from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware import Middleware

from app.middleware.log_request import LogRequestMiddleware
from app.routes.answer.routes import router as answer_router
from app.routes.ask.routes import router as ask_router
from app.routes.welcome.routes import router as home_router
from logger import logger

middleware = [
    Middleware(LogRequestMiddleware),
]

app = FastAPI(middleware=middleware)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home_router)
app.include_router(ask_router, prefix="/ask")
app.include_router(answer_router, prefix="/answer")

templates = Jinja2Templates(directory="app/templates")

if __name__ == "__main__":
    import uvicorn

    logger.info("starting in __main__")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
