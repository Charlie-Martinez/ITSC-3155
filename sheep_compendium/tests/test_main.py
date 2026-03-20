# Import TestClient to simulate API requests
from fastapi.testclient import TestClient
# Import the FastAPI app instance from the controller module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

# Define a test function for reading a specific sheep
def test_read_sheep():
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

# Define a test function for adding a new sheep
def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format.
    new_sheep = {
        "id": 7,
        "name": "Vash",
        "breed": "Babydoll",
        "sex": "ram"
    }

    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    #  Arguments should be your endpoint and new sheep data
    response = client.post("/sheep", json=new_sheep)

    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep

    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    #  include an assert statement to see if the new sheep data can be retrieved.
    get_response = client.get("/sheep/7")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep

def test_delete_sheep():
    # Create the sheep to be deleted
    new_sheep = {
        "id": 8,
        "name": "Wolfwood",
        "breed": "Suffolk",
        "sex": "ram"
    }

    # Send POST request to create the sheep
    create_response = client.post("/sheep", json=new_sheep)
    assert create_response.status_code == 201

    # Send DELETE request to the endpoint
    response = client.delete("/sheep/8")

    # Assert that response code is 200 (OK)
    assert response.status_code == 200

def test_update_sheep():
    # Create the sheep to be deleted
    new_sheep = {
        "id": 9,
        "name": "Original",
        "breed": "Cool breed",
        "sex": "ewe"
    }

    # Send POST request to create the sheep
    create_response = client.post("/sheep", json=new_sheep)
    assert create_response.status_code == 201

    # Create the updated sheep data
    updated_sheep = {
        "id": 9,
        "name": "Updated",
        "breed": "Another breed",
        "sex": "ram"
    }

    # Send PUT request to update the sheep
    update_response = client.put("/sheep/9", json=updated_sheep)

    # Assert that response code is 200 (OK)
    assert update_response.status_code == 200
    # Assert JSON matches the updated sheep data
    assert update_response.json() == updated_sheep

def test_get_all_sheep():
    # Send GET request to endpoint
    response = client.get("/sheep")

    # Assert response code is 200(OK)
    assert response.status_code == 200

    # Store response in list and assert list has the original 6 sheep
    all_sheep = response.json()
    assert len(all_sheep) >= 6
