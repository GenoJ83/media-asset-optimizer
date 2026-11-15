def format_savings_table(total_in: int, total_out: int) -> str:
    pct = round((total_in - total_out) / total_in * 100, 1) if total_in else 0
    return f'Original: {total_in//1024}KB -> Optimized: {total_out//1024}KB | Savings: {pct}%'
