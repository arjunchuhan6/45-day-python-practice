#nstall fastapi 
#pip install fastAPI
#pip install "uvicorn[standard]" 


# Install FastAPI and Uvicorn: python -m pip install fastapi uvicorn
from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a simple GET endpoint
@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}

#for running the app, use the command: uvicorn program_1:app --reload
#python -m uvicorn program_1:app --reload