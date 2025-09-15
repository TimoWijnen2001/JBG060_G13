# Here we have to give an overview of our project

# Notes i dont want to forget

- Optionalyl we can use ROI, we can use provided segmentation data or point labels grown into masks to focus bleaching classification strictly on coral pixels, this could cut the number of white sand = bleached flash positives and enables % bleached cover

- i am putting as many comments in code as possible so everyone, including myself, can understand more whats going on, since i prefer to build the code slowly and understanding whats going on then mass producing malfunctioning scripts.

after all the todos are done run this:

# from project/ root

python -m catalog.build_catalog \
  --config configs/datasets.bleaching.yaml \
  --out outputs/bleaching_catalog.csv \
  --only RS_BLEACHING SEGMENTED_SEAVIEW_SUBSET \
  --limit 200

this is the order we should do it in, if someones works on something, please put your name so that others know, and the next person can take on the next task:

1. Fill load_profiles (YAML → DatasetProfile). (DAVID M)

2. Implement list_images and mask inference for one dataset (e.g., RS_BLEACHING).

3. Add QC: readability + size match flags.

4. Write CSV, run with --limit 50, spot-check in the sanity notebook.

5. Add the second dataset (segmented Seaview); extend mask inference rules.

6. Add points support (Seaview): implement find_points_file.

7. Add context parsing (site/transect/date) if the folder names encode them.
