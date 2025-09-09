from fastapi.testclient import TestClient
from unittest.mock import patch
from notificationService.api.message_service import app
from notificationService.api.model.response import Response

client = TestClient(app)

test_data = {
    "sender_contact": "+14155238887",
    "receiver_contact": "+",
    "message_text": "Hello from test!"
}

# Success Case
@patch("notificationService.api.message_service.send_whatsapp_message")
def test_message_success(mock_send):
    mock_send.return_value = "SM134567891"

    response = client.post("/message", json=test_data)

    assert response.status_code == 200
    assert response.json()["status"] == Response.SUCCESS.value
    assert "message_sid" in response.json()
    mock_send.assert_called_once_with(
        sender_contact=test_data["sender_contact"],
        message_text=test_data["message_text"],
        receiver_contact=test_data["receiver_contact"]
    )

# Failure Case
@patch("notificationService.api.message_service.send_whatsapp_message")
def test_message_failure(mock_send):
    mock_send.return_value = None

    response = client.post("/message", json=test_data)

    assert response.status_code == 500
    assert response.json()["detail"] == "Message sending failed"
