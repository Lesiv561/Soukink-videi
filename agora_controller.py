import os
from dotenv import load_dotenv
from agora_token_service import RtcTokenBuilder, RtcRole

load_dotenv()

APP_ID = os.getenv("AGORA_APP_ID")
APP_CERTIFICATE = os.getenv("AGORA_APP_CERTIFICATE")

def generate_agora_token(channel_name: str, uid: int):
    role = RtcRole.PUBLISHER
    expire_time = 3600
    token = RtcTokenBuilder.buildTokenWithUid(
        APP_ID, APP_CERTIFICATE, channel_name, uid, role, expire_time
    )
    return {"token": token}
