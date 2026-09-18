#use path parameters
import uvicorn
import fastapi

app = fastapi.FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)