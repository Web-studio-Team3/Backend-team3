from bson import ObjectId

from app.infrastracture.connect import database
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestUser:
    def test_sing_up(self):
        response = client.post(
            "/api/users/sign_up",
            json={
                "email": "1",
                "raw_password": "1",
                "full_name": "1",
                "date_of_birth": "01.01.2000",
                "picture": "65d209eef62270bb95e1be84"
            }
        )
        assert response.status_code == 200
        assert response.json() == {
            "chat_message": "user successfully created"
        }

    def test_sing_in(self):
        response = client.post(
            "/api/users/sing_in",
            json={
                "email": "1",
                "raw_password": "1"
            }
        )
        assert response.status_code == 200

    def test_delete(self):
        response = client.delete(
            "/api/users/"
        )
        assert response.status_code == 200

    def test_get_user(self):
        response = client.get("/api/users/info/b5893c06625d65cfbf822e6e")
        assert response.status_code == 200


class TestChat:
    def test_create_chat(self):
        response = client.post(
            "/api/chat/{item_id}/{chat_id}?seller_id=65c397bae1756a2508104f27&buyer_id=65ca4a46d64f34e484ba389c"
        )
        assert response.status_code == 200

    def test_get_chat(self):
        response = client.post(
            "/api/chat/{item_id}/{chat_id}?seller_id=65c397bae1756a2508104f27&buyer_id=65ca4a46d64f34e484ba389c"
        )
        assert response.status_code == 200

    def test_delete_chat(self):
        response = client.post(
            "/api/chat/{item_id}/{chat_id}?seller_id=65c397bae1756a2508104f27&buyer_id=65ca4a46d64f34e484ba389c"
        )
        assert response.status_code == 200
    def test_update_chat(self):
        response = client.post(
            "/api/chat/{item_id}/{chat_id}?seller_id=65c397bae1756a2508104f27&buyer_id=65ca4a46d64f34e484ba389c"
        )
        assert response.status_code == 200
