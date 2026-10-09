def prevent_zip_bomb(file_bytes: int, max_limit: int = 100_000_000):
    if file_bytes > max_limit: raise ValueError('Image exceeds safety memory threshold')
