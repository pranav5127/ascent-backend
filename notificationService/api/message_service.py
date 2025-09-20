from fastapi import FastAPI
import uvicorn
from notificationService.api.model.api_data import ApiData
from notificationService.service.whatsapp_service import send_whatsapp_message
from notificationService.api.model.response import Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/message")
async def message(data: ApiData):
    try:
        message_sid = send_whatsapp_message(
            sender_contact=data.sender_contact,
            message_text=data.message_text,
            receiver_contact=data.receiver_contact
        )

        if not message_sid:
            return JSONResponse(
                status_code=500,
                content={
                    "status": Response.ERROR.value,
                    "detail": "Message sending failed"
                }
            )

        return {
            "status": Response.SUCCESS.value,
            "message_sid": message_sid
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": Response.ERROR.value,
                "detail": str(e)
            }
        )

if __name__ == "__main__":
    uvicorn.run("notificationService.api.message_service:app", host="0.0.0.0", port=42000, log_level="info")



