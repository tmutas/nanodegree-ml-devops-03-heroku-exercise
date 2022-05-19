"""Testing requests to API"""
import pytest
from fastapi.testclient import TestClient
from testapp.api import apiapp

client = TestClient(apiapp)


vals = [(0, 5), (1, 5), (136,50), (3603,5624636), (2465245,356146)]

wrong_paths = ["/foo", "/fsghd", "/bar/130/", "/bar/130/ggla"]

@pytest.mark.parametrize("val,query", vals)
def test_get_items_default(val, query):
    r = client.get(f"/items/{val}")
    assert r.status_code == 200
    assert r.json() == {"data" : f"Gotten {val} with query param 1"}

@pytest.mark.parametrize("val,query", vals)
def test_get_items_query(val,query):
    r = client.get(f"/items/{val}?query={query}")
    assert r.status_code == 200
    assert r.json() == {"data" : f"Gotten {val} with query param {query}"}

@pytest.mark.parametrize("path_name", wrong_paths)
def test_wrong_path(path_name):
    r = client.get(path_name)
    assert r.status_code == 404

