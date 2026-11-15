from pydantic import BaseModel
class MediaAsset(BaseModel):
    path: str
    original_bytes: int
    optimized_bytes: int = 0
    format: str
