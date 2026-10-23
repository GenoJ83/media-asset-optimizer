# Architecture

```mermaid
flowchart LR
    Raw[Raw Images] --> Stripper[EXIF Stripper]
    Stripper --> Resizer[Aspect Resizer]
    Resizer --> WebP[WebP Encoder]
    WebP --> Out[Optimized Assets]
```
