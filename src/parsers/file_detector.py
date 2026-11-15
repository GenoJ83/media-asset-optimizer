import os
SUPPORTED = {'.png', '.jpg', '.jpeg', '.webp', '.tiff'}
def is_supported_image(path: str) -> bool:
    return os.path.splitext(path.lower())[1] in SUPPORTED
