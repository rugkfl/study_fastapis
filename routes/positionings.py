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
@router.get("/forms",response_class=HTMLResponse)
async def form(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/forms.html", context={'request':request})

@router.get("/grids",response_class=HTMLResponse)
async def grid(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/grids.html", context={'request':request})

@router.get("/standards",response_class=HTMLResponse)
async def standard(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/standards.html", context={'request':request})

@router.get("/tables",response_class=HTMLResponse)
async def table(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/tables.html", context={'request':request})

#@ = Annotation  / 체질을 바꿔주는 역할 / 웹에서 펑션 호출

