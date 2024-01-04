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
@router.get("/buttons",response_class=HTMLResponse)
async def button(request:Request) :
    pass 
    return templates.TemplateResponse(name="gadgets/buttons.html", context={'request':request})

#@ = Annotation  / 체질을 바꿔주는 역할 / 웹에서 펑션 호출

@router.get("/cards")
# request = Request()
async def cards(request:Request) :
    # request.query_params
    # QueryParams('name=kim+gyungha&email=rugfkl%40naver.com')
    # dict(request.query_params)
    # {'name': 'kim gyungha', 'email': 'rugfkl@naver.com'}
    return templates.TemplateResponse(name="gadgets/cards.html", context={'request':request})

@router.post("/cards")
async def cards_post(request:Request) :
    # request.query_params
    # QueryParams('')
    # await request.form()
    # FormData([('name', 'kim gyungha'), ('email', 'rugfkl@naver.com')])
    # dict(await request.form())
    # {'name': 'kim gyungha', 'email': 'rugfkl@naver.com'}
    # form_datas = await request.form()
    # dict(form_datas)
    pass 
    return templates.TemplateResponse(name="gadgets/cards.html", context={'request':request})

@router.get("/colors",response_class=HTMLResponse)
async def color(request:Request) :
    pass 
    return templates.TemplateResponse(name="gadgets/colors.html", context={'request':request})

@router.get("/containers",response_class=HTMLResponse)
async def container(request:Request) :
    pass 
    return templates.TemplateResponse(name="gadgets/containers.html", context={'request':request})