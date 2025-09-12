# color legends & helpers per dataset

from typing import Dict, Tuple

RGB = Tuple[int,int,int]

PALETTES: Dict[str, Dict[str, RGB]] = {
    # For health masks (RS Bleaching example)
    "rs_bleaching_v1": {
        "healthy": (255, 0, 0),
        "bleached": (0, 0, 255),
        "dead": (0, 0, 0),
    },
    # For structure masks (Segmented Seaview example)
    "seaview_segmented_v1": {
        "hard_coral": (255, 0, 0),
        "soft_coral": (0, 0, 255),
    },
}

def known_palette(key: str) -> Dict[str, RGB]:
    # TODO: raise a clear error if key not in PALETTES
    return PALETTES[key]