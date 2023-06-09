from torch import nn
import torch as t
from torch.nn import functional as F

class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.seq = t.nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=6, kernel_size=5),
            nn.MaxPool2d(kernel_size=3),
            nn.Conv2d(in_channels=6, out_channels=6, kernel_size=3),
            nn.AvgPool2d(kernel_size=5)
        )
        
        self.fc = t.nn.Sequential(
            nn.Linear(1176, 32),
            nn.ReLU(),
            nn.Linear(32, 8),
        )

    def forward(self, x):
        x = self.seq(x)
        x = x.flatten(start_dim=1)
        x = self.fc(x)
        return x