import json
def export_savings_json(report: dict) -> str:
    return json.dumps(report, indent=2)
