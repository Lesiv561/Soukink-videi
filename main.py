from fastapi import FastAPI
from routes.call_routes import router as call_router

app = FastAPI()

# Register Routes
app.include_router(call_router)

@app.get("/")
def root():
    return {"message": "Video Call Backend Active"}
