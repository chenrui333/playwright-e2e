import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    yield


def test_course_api():
    course_data = {
        "course_name": "Test Course",
        "credits": 3,
        "department": "Test Department",
        "semester": "Fall",
        "year": 2023,
    }

    # test create api
    course_resp = client.post("/courses", json=course_data)
    assert course_resp.status_code == 200

    created_course = course_resp.json()
    course_id = created_course["course_id"]

    # test read api
    read_resp = client.get(f"/courses/{course_id}")
    assert read_resp.status_code == 200
    read_course = read_resp.json()
    assert read_course["course_name"] == course_data["course_name"]

    # test update api
    updated_course_data = {
        "course_name": "Updated Course",
        "credits": 4,
        "department": "Updated Department",
        "semester": "Spring",
        "year": 2024,
    }

    update_resp = client.put(f"/courses/{course_id}", json=updated_course_data)
    assert update_resp.status_code == 200
    updated_course = update_resp.json()
    assert updated_course["course_name"] == updated_course_data["course_name"]
    assert updated_course["credits"] == updated_course_data["credits"]
    assert updated_course["department"] == updated_course_data["department"]

    # test delete api
    delete_resp = client.delete(f"/courses/{course_id}")
    assert delete_resp.status_code == 200

    # test read deleted course
    read_deleted_resp = client.get(f"/courses/{course_id}")
    assert read_deleted_resp.status_code == 404
