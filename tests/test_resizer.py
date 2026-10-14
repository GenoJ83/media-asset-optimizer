from src.engine.resizer import calculate_dimensions
def test_resizer():
    w, h = calculate_dimensions(3000, 2000, 1500)
    assert w == 1500 and h == 1000
