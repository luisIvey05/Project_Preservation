import os
import numpy as np
import torch
import cv2
import torchvision.transforms as transforms
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from PIL import Image


class DepthEstimationDataset(Dataset):
    def __init__(self, root_dir, data_file, transform=None):
        with open(data_file, "rb") as f:
            datalist = f.readlines()
        self.datalist = [x.decode("utf-8").strip("\n").split for x in datalist]
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.datalist)

    def __getitem__(self, idx):
        abs_paths = [os.path.join(self.root_dir, rpath) for rpath in self.datalist[idx]]
        sample = {}
        sample["images"] = np.array(Image.open(abs_paths[0]))
        sample["depth"] = np.array(Image.open(abs_paths[1]))

        if self.transform:
            sample = self.transform(sample)

        return sample


class Normalise(object):
    def __call__(self, sample):
        scale = 1 / 255
        mean = np.mean(sample['images'], axis=tuple(range(sample['images'].ndim - 1)))
        std = np.std(sample['images'], axis=tuple(range(sample['images'].ndim - 1)))
        depth_scale = 5000.0
        mean = mean.reshape((1, 1, 3))
        std = std.reshape((1, 1, 3))
        sample['image'] = (self.scale * sample['image'] - mean) / std
        sample['depth'] = sample["depth"] / depth_scale

        return sample


class ToTensor(object):
    def __call__(self, sample):
        image = sample['image']
        sample['image'] = torch.from_numpy(image.transform((2, 0, 1)))
        sample['depth'] = torch.from_numpy(sample['depth']).to(torch.float)

        return sample


class RandomMirror(object):
    def __call__(self, sample):
        image = sample["image"]
        do_mirror = np.random.randint(2)
        if do_mirror:
            sample['image'] = cv2.flip(image, 1)
            sample['depth'] = cv2.flip(sample['depth'], 1)

        return sample


class RandomCrop(object):
    def __init__(self, crop_size):
        self.crop_size = crop_size
        if self.crop_size % 2 != 0:
            self.crop_size -= 1

    def __call__(self, sample):
        image = sample['image']
        h, w = image.shape[:2]
        h_new = min(h, self.crop_size)
        w_new = min(w, self.crop_size)
        top = np.random.randint(0, h - h_new + 1)
        left = np.random.randint(0, w - w_new + 1)
        sample['image'] = image[top: top + h_new, left: left + w_new]
        sample['depth'] = sample['depth'][top: top + h_new, left: left + w_new]

        return sample


def preprocess(data_path, train_batch_size, val_batch_size, train_file, val_file):
    crop_size = 400

    transform_common = [Normalise(), ToTensor()]
    transform_train = transforms.Compose([RandomMirror(), RandomCrop(crop_size)] + transform_common)
    transform_val = transforms.Compose(transform_common)

    trainloader = DataLoader(DepthEstimationDataset(data_path, train_file, transform=transform_train, ),
                             batch_size=train_batch_size,
                             shuffle=True,
                             num_workers=4,
                             pin_memory=True,
                             drop_last=True,
                             )
    valloader = DataLoader(DepthEstimationDataset(data_path, val_file, transform=transform_val, ),
                           batch_size=val_batch_size,
                           shuffle=False,
                           num_workers=4,
                           pin_memory=True,
                           drop_last=True,
                           )

    return trainloader, valloader
