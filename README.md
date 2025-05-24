# Video Call Backend (Agora + FastAPI)

## Setup
1. Fill out `.env` with your Agora App ID and Certificate.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   uvicorn main:app --reload
   ```

## Routes
- `POST /generate-token` — Get an Agora RTC token
