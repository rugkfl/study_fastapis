from fastapi import FastAPI

app = FastAPI()

from routes.homes import router as homes_router
from routes.gadgets import router as gadgets_router
from routes.positionings import router as positionings_router
from routes.users import router as users_router
app.include_router(homes_router, prefix='/home')
app.include_router(gadgets_router, prefix='/gadgets')
app.include_router(positionings_router, prefix='/positionings')
app.include_router(users_router, prefix="/users")

from fastapi import Request
from fastapi.templating import Jinja2Templates

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

@app.get("/")
async def index(request:Request):
    # return {"message": "Kim GyungHa World!"}
    # html 호출
    return templates.TemplateResponse("main.html"
                                      ,{'request':request})


# @app.get("/index")
# async def index(request:Request):
#     # return {"message": "Kim GyungHa World!"}
#     # html 호출
#     return templates.TemplateResponse("index.html"
#                                       ,{'request':request})


