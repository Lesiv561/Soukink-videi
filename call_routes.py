from fastapi import APIRouter, Request
from controllers.agora_controller import generate_agora_token

router = APIRouter()

@router.post("/generate-token")
async def get_token(request: Request):
    data = await request.json()
    channel_name = data.get("channelName")
    uid = data.get("uid")
    return generate_agora_token(channel_name, uid)
