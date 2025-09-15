# quick quality checks (size match, readability, heuristics)

from pathlib import Path
from typing import List, Tuple
from PIL import Image

def readable_image(path: Path) -> bool:
    # TODO: open with PIL inside try/except; return False if fails
    return True

def image_size(path: Path) -> Tuple[int,int]:
    # TODO: return (width,height)
    return 0, 0

def size_match(img_wh, mask_wh) -> bool:
    # TODO: exact match for now (no resizing in catalog)
    return True

def basic_flags(img_path: Path, mask_path: Path) -> List[str]:
    """Return a list of qc flags for this pair."""
    # TODO: implement: unreadable, mask_missing, size_mismatch, empty_mask?
    return []
