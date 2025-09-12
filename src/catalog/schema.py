# the canonical row schema (+ helpers to validate rows)

from dataclasses import dataclass, asdict
from typing import Optional, Dict, List

@dataclass
class CatalogRow:
    dataset_name: str
    dataset_group: str
    image_path: str
    mask_path: str
    label_type: str
    palette_key: Optional[str]
    has_points: bool
    points_bath: str
    site: Optional[str]
    transect: Optional[str]
    date: Optional[str]
    width: Optional[int]
    height: Optional[int]
    qc_flags: Optional[str]
    
    