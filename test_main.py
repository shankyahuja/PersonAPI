from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_person():
    response = client.get("/person/1", headers={"access_token": "1234567asdfgh"})
    assert response.status_code == 200
    assert response.json() == {
        "id":1,
        "first_name":"Buiron",
        "last_name":"Avo",
        "email":"bavo0@uiuc.edu",
        "gender":"Polygender",
        "ip_address":"222.199.35.144",
        "country_code":"RU"
    }

def test_read_person_bad_token():
    response = client.get("/person/1", headers={"access_token": "badtoken"})
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate credentials"}


def test_read_inexistent_person():
    response = client.get("/person/99999", headers={"access_token": "1234567asdfgh"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Person not found"}


def test_create_person():
    response = client.post(
        "/person/",
        headers={"access_token": "1234567asdfgh"},
        json={"id":1001,"first_name":"Katha1","last_name":"Carroll1","email":"kcarrollrr1@prweb.com","gender":"Bigender","ip_address":"66.199.132.198","country_code":"RU"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id":1001,
        "first_name":"Katha1",
        "last_name":"Carroll1",
        "email":"kcarrollrr1@prweb.com",
        "gender":"Bigender",
        "ip_address":"66.199.132.198",
        "country_code":"RU"
    }


def test_create_person_bad_token():
    response = client.post(
        "/person/",
        headers={"access_token": "badtoken"},
        json={"id":1001,"first_name":"Katha1","last_name":"Carroll1","email":"kcarrollrr1@prweb.com","gender":"Bigender","ip_address":"66.199.132.198","country_code":"RU"},
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate credentials"}