import uvicorn
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main_function():
    return {"status": "Api running"}


if __name__ == "__main__":
    config = {
        "server": "127.0.0.1",
        "port": 5000,
        "log": "info"
    }
    uvicorn.run(
        "app:app",
        host=config["server"],
        port=config["port"],
        log_level=config["log_level"],
        reload=True,
    )