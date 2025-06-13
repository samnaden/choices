from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

import app.routes.ask.models as models
import app.services.questions as questions_service
import app.services.visitors as visitors_service

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


async def _parse_ask_form(request: Request) -> models.AskForm:
    form_data = await request.form()
    name = form_data.get("name", "")
    question = form_data.get("question", "")
    options = form_data.getlist("options")
    return models.AskForm(name=name, question=question, options=options)


@router.get("", response_class=HTMLResponse)
async def ask_screen(request: Request) -> Response:
    return templates.TemplateResponse("ask/index.html", {"request": request})


@router.post("", response_class=HTMLResponse)
async def handle_ask(
    request: Request,
    form: models.AskForm = Depends(_parse_ask_form),
) -> Response:
    visitor_id = visitors_service.insert_visitor(visitor_name=form.name)
    questions_service.insert_question(
        visitor_id=visitor_id, question_text=form.question, options=form.options
    )
    return RedirectResponse(
        url=f"/answer?name={form.name}", status_code=status.HTTP_303_SEE_OTHER
    )
