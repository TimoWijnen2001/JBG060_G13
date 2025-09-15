# path walking, mask inference, palette probing

from pathlib import Path
from typing import Iterable, Optional, Tuple, Dict
from .dataset_profiles import DatasetProfile
from .schema import CatalogRow

def list_images(root: Path, pattern: str) -> Iterable[Path]:
    """Yield all image files under root matching glob pattern."""
    # TODO: implement Path(root).glob(pattern) with filtering by ext
    yield from ()

def infer_mask_path(img: Path, root: Path, profile: DatasetProfile) -> Optional[Path]:
    """Return expected mask path or None using profile.mask rules."""
    # TODO: implement "same_basename" or "suffix" logic
    return None

def find_points_file(img: Path, root: Path, profile: DatasetProfile) -> Optional[Path]:
    """Return points annotation path for this image if present (Seaview)."""
    # TODO: implement matcher (e.g., by filename stem)
    return None

def parse_context_from_path(img: Path, dataset_name: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """Try to extract site/transect/date from folder structure or filename."""
    # TODO: implement a forgiving parser; return (site, transect, date)
    return None, None, None
