#add authenticaton to your api
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# --- Config (use environment variables in production!) ---
SECRET_KEY = "change-this-to-a-long-random-secret-key"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Fake user database (replace with a real DB) ---
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

USERS = {
    "alice": {
        "username": "alice",
        "hashed_password": hash_password("secret123"),
        "role": "admin",
    }
}

# --- Helpers ---
def authenticate_user(username: str, password: str):
    user = USERS.get(username)
    if not user or not bcrypt.checkpw(password.encode(), user["hashed_password"].encode()):
        return None
    return user

def create_access_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in USERS:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return USERS[username]

# --- Routes ---
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return {"access_token": create_access_token(user["username"]), "token_type": "bearer"}

@app.get("/public")
def public():
    return {"message": "Anyone can access this"}

@app.get("/protected")
def protected(user: dict = Depends(get_current_user)):
    return {"message": f"Hello {user['username']}! You are authenticated."}

@app.get("/admin")
def admin_only(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return {"message": "Welcome, admin!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)