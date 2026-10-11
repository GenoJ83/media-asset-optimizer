def compute_aggregate_metrics(assets: list):
    in_bytes = sum(a.original_bytes for a in assets)
    out_bytes = sum(a.optimized_bytes for a in assets)
    return {'total_in': in_bytes, 'total_out': out_bytes}
