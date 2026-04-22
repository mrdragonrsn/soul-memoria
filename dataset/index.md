# Dataset - Guia

## Estrutura de Dados

### Treinamento (Training Set)
- 60-80% dos dados
- Usado para treinar modelo

### Validação (Validation Set)
- 10-20% dos dados
- Ajuste de hiperparâmetros
- Evitar overfitting

### Teste (Test Set)
- 10-20% dos dados
- Avaliar performance final

## Criar Dataset PyTorch

```python
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
```

## DataLoader

```python
dataloader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4
)
```

## Augmentação

```python
from torchvision import transforms

transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.2),
    transforms.ToTensor(),
])
```

## Referências
[[preprocessamento/index]]
[[avaliacao/index]]