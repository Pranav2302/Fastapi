from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.database import get_db
from app.models.user import User
from app.auth import create_access_token
from passlib.context import CryptContext

#tags - groups all the routes under router of auth category 
router = APIRouter(tags=["auth"]) #used for api documentation , help in organize and group endpoints in auto generated openapi(swagger)docs
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #password hashing
# schemes - any hashing algorithm can be use "argon2" if deprecated then auto handling
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/login")
#dependencies (objects, functions) are automatically provided to a function/class instead of being created manually inside it.
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.username == form_data.username))
    user = result.scalar()  # Returns first match or none 
    
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},  #tells client that it needs to authenticate using Bearer Token authentication.
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(username: str, password: str, db: AsyncSession = Depends(get_db)):   #type hint is used as parameter and type of that parameter
    result = await db.execute(select(User).filter(User.username == username))
    if result.scalar():
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    hashed_password = get_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    await db.commit()
    return {"message": "User created successfully"}


#if doing maually without dependence injection 
#@app.post("/login")
#async def login(username: str = Form(), password: str = Form()):

#Instead of manually parsing username and password from the request, FastAPI automatically extracts and validates them.

#this is process happens in parameter while using dependcy
'''Extracts the username & password.
Validates them using OAuth2PasswordRequestForm.
Passes the validated form_data to login().'''