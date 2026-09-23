def calculate_dimensions(w: int, h: int, max_w: int):
    if w <= max_w: return w, h
    ratio = max_w / float(w)
    return max_w, int(h * ratio)
