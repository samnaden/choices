from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

import app.routes.answer.models as models
import app.services.answers as answers_service
import app.services.questions as questions_service

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


async def _parse_answer_form(request: Request) -> models.AnswerForm:
    form_data = await request.form()
    name = form_data.get("name", "")
    answers = {
        k.replace("question_", ""): v
        for k, v in form_data.items()
        if k.startswith("question_")
    }
    return models.AnswerForm(name=name, answers=answers)


@router.get("", response_class=HTMLResponse)
async def answer_screen(request: Request, name: str = "") -> Response:
    questions = questions_service.get_all_questions()

    return templates.TemplateResponse(
        "answer/index.html",
        {"request": request, "name": name, "questions": questions},
    )


@router.post("", response_class=HTMLResponse)
async def handle_answer(
    request: Request,
    form: models.AnswerForm = Depends(_parse_answer_form),
) -> Response:
    answers_service.update_answer_votes(list(form.answers.values()))
    return RedirectResponse(
        url=f"/answer?name={form.name}", status_code=status.HTTP_303_SEE_OTHER
    )
