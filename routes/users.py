from fastapi import APIRouter

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

# 회원가입 form/users/form -> users/insert.html
@router.get("/form")  # 어노테이션 (웹에서 업무(function) 호출)
async def insert(request : Request):
   return templates.TemplateResponse(name="users/insert.html", context={'request':request})

@router.post("/form")  # 어노테이션 (웹에서 업무(function) 호출)
async def insert(request : Request):
   return templates.TemplateResponse(name="users/insert.html", context={'request':request})



# 로그인 /users/insert -> users/login.html
@router.get("/login")  # 어노테이션 (웹에서 업무(function) 호출)
async def insert(request : Request):
   pass #biz
   return templates.TemplateResponse(name="users/logins.html", context={'request':request})

# 로그인 /users/insert -> users/login.html
@router.post("/login")  # 어노테이션 (웹에서 업무(function) 호출)
async def insert(request : Request):
   pass #biz
   return templates.TemplateResponse(name="users/logins.html", context={'request':request})




# 회원리스트 /users/list -> users/list.html
@router.get("/list") 
async def insert(request : Request):
   return templates.TemplateResponse(name="users/lists.html", context={'request':request})

@router.post("/list") 
async def insert(request : Request):
   return templates.TemplateResponse(name="users/lists.html", context={'request':request})


# 회원 상세정보 /users/reads -> users/reads.html
# Path parameters : /users/read/id or /users/read/unique_name
@router.get("/read/{object_id}")  
async def insert(request : Request, object_id):
   return templates.TemplateResponse(name="users/reads.html", context={'request':request})

@router.post("/read/{object_id}")  
async def insert(request : Request, object_id):
   return templates.TemplateResponse(name="users/reads.html", context={'request':request})



