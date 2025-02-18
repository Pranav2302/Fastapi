from jose import JWTError, jwt
from datetime import datetime, timedelta

# Secret key and algorithm (like JWT.sign in Node.js)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    expires = datetime.utcnow() + timedelta(minutes=30)
    data.update({"exp": expires})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)