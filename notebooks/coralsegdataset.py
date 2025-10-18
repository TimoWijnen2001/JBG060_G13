import albumentations as A
import cv2
from torch.utils.data import Dataset
from albumentations.pytorch import ToTensorV2

class CoralSegDataset(Dataset):
    def __init__(self, df, augment=False):
        self.df = df
        self.augment = augment
        self.transform = self.get_transform(augment)

    def __len__(self):
        return len(self.df)

    def get_transform(self, augment):
        if augment:
            return A.Compose([
                A.HorizontalFlip(p=0.5),    # type: ignore
                A.VerticalFlip(p=0.5),
                A.RandomRotate90(p=0.5),
                A.RandomBrightnessContrast(p=0.5),
                A.CLAHE(clip_limit=2.0, tile_grid_size=(8,8), p=0.3),
                A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=15, val_shift_limit=10, p=0.5),
                A.GaussianBlur(blur_limit=3, p=0.3),
                A.CoarseDropout(max_holes=8, max_height=32, max_width=32, fill_value=0, p=0.3),
                A.Normalize(),
                ToTensorV2()])
        else:
            return A.Compose([
                A.Normalize(),
                ToTensorV2()
            ])

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        image = cv2.imread(row["image_resized"])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mask  = cv2.imread(row["mask_resized"], cv2.IMREAD_GRAYSCALE)
        mask  = (mask > 127).astype("float32")

        transformed = self.transform(image=image, mask=mask)
        return transformed["image"], transformed["mask"].unsqueeze(0)