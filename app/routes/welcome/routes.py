from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

import app.routes.welcome.models as models

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


def _parse_welcome_form(
    name: str = Form(...),
    action: str = Form(...),
) -> models.WelcomeForm:
    return models.WelcomeForm(name=name, action=action)


@router.get("/", response_class=HTMLResponse)
async def welcome_screen(request: Request) -> Response:
    return templates.TemplateResponse("welcome/index.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
async def handle_home(
    request: Request,
    info: models.WelcomeForm = Depends(_parse_welcome_form),
) -> Response:
    if info.action == "ask":
        return templates.TemplateResponse(
            "ask/index.html", {"request": request, "name": info.name}
        )
    elif info.action == "answer":
        return RedirectResponse(
            url=f"/answer?name={info.name}", status_code=status.HTTP_303_SEE_OTHER
        )
    return RedirectResponse("/", status_code=303)
