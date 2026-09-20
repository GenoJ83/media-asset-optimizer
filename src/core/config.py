from pydantic import BaseModel
class OptimizerConfig(BaseModel):
    quality: int = 82
    max_width: int = 2560
    strip_metadata: bool = True
    target_format: str = 'webp'
