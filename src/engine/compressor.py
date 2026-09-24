def estimate_savings(orig: int, opt: int) -> float:
    if orig == 0: return 0.0
    return round((orig - opt) / orig * 100.0, 2)
