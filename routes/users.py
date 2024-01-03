from fastapi import APIRouter

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

# 회원가입
@router.get("/insert")  # 어노테이션 (웹에서 업무(function) 호출)
async def insert(request : Request):
   return templates.TemplateResponse(name="users/insert.html", context={'request':request})


