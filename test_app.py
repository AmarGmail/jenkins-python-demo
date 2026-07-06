from app import add
from app import area_ractangle

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert add(10, 30) == 40

def test_area():
    assert area_ractangle(1, 4) == 4
    assert area_ractangle(-3, 4) == -12
    assert area_ractangle(5, 6) == 30
    assert area_ractangle(0, 10) == 0
