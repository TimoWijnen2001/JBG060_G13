# CLI entrypoint, the script you run from the terminal to start the program

import argparse, csv, json
from pathlib import Path
from typing import List
import yaml

from .dataset_profiles import DatasetProfile, MaskRule, PointsRule
from .schema import CatalogRow, validate_row, REQUIRED_COLUMNS
from .scanners import list_images, infer_mask_path, find_points_file, parse_context_from_path
from .qc import readable_image, image_size, basic_flags

def load_profiles(cfg_path: Path) -> (Path, List[DatasetProfile]):
    # TODO: read YAML and instantiate DatasetProfile objects
    # return root_path, profiles
    raise NotImplementedError

def build_rows_for_dataset(root: Path, profile: DatasetProfile) -> List[CatalogRow]:
    rows: List[CatalogRow] = []
    # TODO:
    # 1) iterate images (respect a --limit if provided; pass via profile or args)
    # 2) infer mask_path (or "") and points_path (or "")
    # 3) parse site/transect/date
    # 4) measure width/height
    # 5) compute qc_flags
    # 6) assemble CatalogRow, validate_row
    return rows

def write_csv(rows: List[CatalogRow], out_csv: Path) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=REQUIRED_COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow(r.to_dict())

def main():
    ap = argparse.ArgumentParser(description="Build unified catalog CSV from multiple datasets.")
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--only", nargs="*", help="Optional list of dataset names to include")
    ap.add_argument("--limit", type=int, default=None, help="Max images per dataset (for dry-run)")
    args = ap.parse_args()

    root, profiles = load_profiles(args.config)
    if args.only:
        profiles = [p for p in profiles if p.name in args.only]

    all_rows: List[CatalogRow] = []
    for prof in profiles:
        rows = build_rows_for_dataset(root, prof)
        # TODO: honor --limit here
        all_rows.extend(rows)

    write_csv(all_rows, args.out)
    print(f"Wrote {len(all_rows)} rows → {args.out}")

if __name__ == "__main__":
    main()
