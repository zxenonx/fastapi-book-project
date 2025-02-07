from tests import client


def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_single_book():
    response = client.get("/books/1")
    assert response.status_code == 201
    assert response.json()["title"] == "The Hobbit"
    assert response.json()["author"] == "J.R.R. Tolkien"
