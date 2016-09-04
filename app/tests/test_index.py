def test_index(app):
    response = app.get("/")
    assert response.status_code == 200
    html = response.data.decode("utf-8")
    assert "HELLO!" in html
