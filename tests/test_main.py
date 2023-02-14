from fastapi.testclient import TestClient
from src.main import app


class TestMain:

    def test_read_root(self):
        # given
        client = TestClient(app)

        # when
        response = client.get("/")

        #then
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}


