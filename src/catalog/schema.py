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
    
    def to_dict(self) -> Dict:
        d = asdict(self) # this converts dataclass into python dict
        d["qc_flags"] = ",".join(self.qc_flags) # turns a "mask_missing","size_mismatch" strin into "mask_missing,size_mismatch"
        return d

REQUIRED_COLUMNS = [
    "dataset_name","dataset_group","image_path","mask_path",
    "label_type","palette_key","has_points","points_path",
    "site","transect","date","width","height","qc_flags"
]

def validate_row(row: CatalogRow) -> None:
    """Assertions and type checks, you can add any if you see 
    that there is anything else we can check, raise if something is off"""
    # task for someone: implementing miniaml checks (for example that requires fields are not empty, etc.
    pass