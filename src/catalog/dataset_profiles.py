# dataclasses describing each dataset's rules

from dataclasses import dataclass
from typing import Optional

@dataclass
class MaskRule:
    dir: str
    naming: str
    suffix: str
    ext: str

@dataclass
class PointsRule:
    dir: str
    matcher: str
    
@dataclass
class DatasetProfile:
    name: str
    group: str
    images_glob: str
    label_type: str
    palette_key: Optional[str]
    has_points: bool
    mask: Optional[MaskRule] = None
    points: Optional[PointsRule] = None