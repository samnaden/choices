from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

import app.routes.ask.models as models

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


def _parse_ask_form(
    name: str = Form(...),
    question: str = Form(...),
) -> models.AskForm:
    return models.AskForm(name=name, question=question)


@router.get("", response_class=HTMLResponse)
async def ask_screen(request: Request) -> Response:
    return templates.TemplateResponse("ask/index.html", {"request": request})


@router.post("", response_class=HTMLResponse)
async def handle_ask(
    request: Request,
    info: models.AskForm = Depends(_parse_ask_form),
) -> Response:
    return templates.TemplateResponse(
        "answer/index.html", {"request": request, "name": info.name}
    )
