import sys
sys.path.append('.')
from main import app
from fastapi.testclient import TestClient
from functions.functions_app import main_calculus


client = TestClient(app)

def test_get_nba_data():
    mock_parameter_1 = {"height_target":139}
    mock_parameter_2 = {"height_target":0}
    response_mock_1 = client.post("/api/v1/find_heights_nba", json=mock_parameter_1)
    response_mock_2 = client.post("/api/v1/find_heights_nba", json=mock_parameter_2)
    assert len(response_mock_1.json()["results"]) > 0
    assert response_mock_1.status_code == 200
    assert response_mock_2.json() =={'results': 'Please enter values greater than zero and of integer type'}
def test_endpoint_not_found():
    response = client.get("/api/v1/fake_resource")
    assert response.status_code == 404
    assert response.json() == {"message": "el recurso solicitado no existe"}


def test_main_calculus_function():
    fake_target_1 = main_calculus(0)
    fake_target_2 = main_calculus(139)
    fake_target_3 = main_calculus("target")
    assert fake_target_1 == {'message': 'Not match found'}
    assert len(fake_target_2) > 0
    assert fake_target_3 == {'error_message': 'please insert integer value'}
    