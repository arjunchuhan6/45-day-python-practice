#use query parameters
import uvicorn
import fastapi

app = fastapi.FastAPI()

@app.get("/search")
def search_items(q: str, limit: int = 10):
    return {"query":"python","limit":5}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)