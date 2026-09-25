def filter_large_assets(assets: list, min_bytes: int = 500000):
    return [a for a in assets if a.original_bytes >= min_bytes]
