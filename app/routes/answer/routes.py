from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

import app.routes.answer.models as models

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


def _parse_answer_form(
    name: str = Form(...),
    answer: str = Form(...),
) -> models.AnswerForm:
    return models.AnswerForm(name=name, answer=answer)


@router.get("", response_class=HTMLResponse)
async def answer_screen(request: Request) -> Response:
    return templates.TemplateResponse("answer/index.html", {"request": request})


@router.post("", response_class=HTMLResponse)
async def handle_answer(
    request: Request,
    info: models.AnswerForm = Depends(_parse_answer_form),
) -> Response:
    return templates.TemplateResponse(
        "answer/index.html", {"request": request, "name": info.name}
    )
