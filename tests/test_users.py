import pytest


@pytest.mark.smoke
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_get_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
    assert  len(response.json())>0


def test_create_post(api_client):
    payload = {
        "title" : "my first posts",
        "body" : "learning automation",
        "userId" : 1
    }
    response = api_client.post("/posts" , payload)
    assert response.status_code ==201
    data = response.json()
    assert data["title"] == "my first posts"
    assert "id" in data

@pytest.mark.parametrize("user_id" ,[1,2,3])
def test_get_single_user(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code ==200
    data = response.json()
    assert  data["id"] == user_id;

def test_get_nonexistent_user(api_client):
    response = api_client.get("/users/9999")
    assert response.status_code == 404
    assert response.json() == {}


def test_response_time_under_threshold(api_client):
    response = api_client.get("/users")
    assert response.status_code ==200
    elapsed = response.elapsed.total_seconds()
    assert elapsed<2, f"API too slow: {elapsed:.2f}s"
