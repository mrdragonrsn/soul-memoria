# Deep Learning - Guia

## O que é Deep Learning
 subset de machine learning que usa redes neurais com múltiplas camadas ocultas (daí "deep" = profundo).

## Arquiteturas

### Conv2D (Convolução 2D)
```python
import torch.nn as nn

conv = nn.Conv2d(
    in_channels=3,    # RGB
    out_channels=64,
    kernel_size=3,
    padding=1
)
```

### Pooling (Subamostragem)
```python
pool = nn.MaxPool2d(kernel_size=2, stride=2)
```

### Dropout (Regularização)
```python
dropout = nn.Dropout(p=0.5)  # 50% desliga neurônios
```

## Pipeline Completo
```python
model = nn.Sequential(
    # Conv + ReLU + Pool
    nn.Conv2d(3, 32, 3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    
    # Flatten
    nn.Flatten(),
    
    # Dense
    nn.Linear(32 * 14 * 14, 10),
    nn.Softmax(dim=1)
)
```

## Quando Usar
- Imagens → Conv2D
- Videos → Conv3D
- Reduzir overfitting → Dropout

## Referências
[[computer_vision/index]]