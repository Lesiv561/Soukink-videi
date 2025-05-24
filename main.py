from fastapi import FastAPI
from routes.call_routes import router as call_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Video Call Backend Active"}

app.include_router(call_router)
