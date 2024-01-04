from fastapi import APIRouter

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")
# home
# @router.get("/", response_class=HTMLResponse)
# async def home():
#     # return {"message": "home World!"}
#     html = "<body> <h2> It's Home.</h2> </body>"
#     return html
@router.get("/",response_class=HTMLResponse)
async def root(request:Request) :
    pass 
    return templates.TemplateResponse(name="homes/standards.html", context={'request':request})

#@ = Annotation  / 체질을 바꿔주는 역할 / 웹에서 펑션 호출

# /home/list
@router.get("/list", response_class=HTMLResponse)  
# 어노테이션 (웹에서 업무(function) 호출)
async def home_list():
    html = "<body> <h2> It's Home List.</h2> </body>"
    return html

# /homes/params_query -> /homes/parameters_query.html 호출
@router.get("/params_query")
async def home(request:Request) :
    pass 
    return templates.TemplateResponse(name="homes/parameters_query.html", context={'request':request})


