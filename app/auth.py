from fastapi import Depends, HTTPException, status  #HTTP_401_UNAUTHORIZED can use 
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt #handling jwt and allow encoding and decoding
from datetime import datetime, timedelta,timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.database import get_db
from app.models.user import User

# Configuration
SECRET_KEY = "pranav"  # a secure secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):   #data type giving here is type hinting , it is done by pydantic which validates the data of incoming reponse, 
    to_encode = data.copy()
    #expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    print("check payload before jwt",to_encode)    #checking
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("check payload after jwt",payload)   #checking 
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    result = await db.execute(select(User).filter(User.username == username))
    user = result.scalar()   # scalar () - Retrieves a single row (or None if not found).
    
    if user is None:
        raise credentials_exception
    return user