from src.engine.compressor import estimate_savings
def test_savings():
    assert estimate_savings(1000, 500) == 50.0
