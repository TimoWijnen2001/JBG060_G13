# coral_dataset.py
import numpy as np
from PIL import Image
from torch.utils.data import Dataset


class CoralDataset(Dataset):
    def __init__(self, df, transform=None):
        self.df = df.reset_index(drop=True)
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.loc[idx]
        img_path = row["image_path"]
        mask_path = row["mask_path"]

        image = np.array(Image.open(img_path).convert("RGB"))
        mask = np.array(Image.open(mask_path).convert("L"))
        mask = (mask > 0).astype(np.float32)

        if self.transform:
            data = self.transform(image=image, mask=mask)
            image = data["image"]
            mask = data["mask"].unsqueeze(0)  # [1,H,W] for BCE/Dice

        return image, mask
