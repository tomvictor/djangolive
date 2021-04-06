from rest_framework.test import APIClient

client = APIClient()


def test_brokers():
    response = client.get("/test/")
    assert response.status_code == 200, f"{response}"
