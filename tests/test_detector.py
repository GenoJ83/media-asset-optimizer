from src.parsers.file_detector import is_supported_image
def test_detector():
    assert is_supported_image('hero.PNG')
    assert not is_supported_image('notes.txt')
