import uvicorn
from fastapi import FastAPI

def init_app():
    apps = FastAPI(
        title="Fast API Store",
        description="Fast API",
        version="1.0.0"
    )

    @apps.get('/')
    def index():
        return "Server is running"

    return apps


app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

