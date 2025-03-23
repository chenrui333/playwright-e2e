import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    yield


def test_students_api():
    student_data = {
        "name": "Test Student",
        "age": 20,
        "enroll_year": 2021,
        "major": "Test Major",
        "gpa": 3.5,
    }

    # test create api
    create_resp = client.post("/students", json=student_data)
    assert create_resp.status_code == 200
    created_student = create_resp.json()
    student_id = created_student["student_id"]
    assert created_student["name"] == student_data["name"]

    # test read api
    read_resp = client.get(f"/students/{student_id}")
    assert read_resp.status_code == 200
    read_student = read_resp.json()
    assert read_student["name"] == student_data["name"]
    assert read_student["age"] == student_data["age"]

    # test update api
    updated_student_data = {
        "name": "Updated Student",
        "age": 21,
        "enroll_year": 2022,
        "major": "Updated Major",
        "gpa": 3.8,
    }

    update_resp = client.put(f"/students/{student_id}", json=updated_student_data)
    assert update_resp.status_code == 200
    updated_student = update_resp.json()
    assert updated_student["name"] == updated_student_data["name"]
    assert updated_student["age"] == updated_student_data["age"]
    assert updated_student["major"] == updated_student_data["major"]

    # test delete api
    delete_resp = client.delete(f"/students/{student_id}")
    assert delete_resp.status_code == 200

    # test read deleted student
    read_deleted_resp = client.get(f"/students/{student_id}")
    assert read_deleted_resp.status_code == 404
