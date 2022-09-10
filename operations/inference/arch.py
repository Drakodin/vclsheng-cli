import torch.nn as nn

class ANN(nn.Module):
    def __init__(self, loss = nn.CrossEntropyLoss(reduction='mean')):
        super().__init__()
        
        self.loss = loss
        self.layers = nn.Sequential(
            nn.Linear(40, 50),
            nn.Dropout(0.4),
            nn.ReLU(),
            nn.Linear(50, 50),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(50, 50),
            nn.Dropout(0.3),
            nn.ReLU(),
        )
        self.classifier = nn.Sequential(
            nn.Linear(50, 2),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        output = None
        x = self.layers(x)
        output = self.classifier(x)
        return output