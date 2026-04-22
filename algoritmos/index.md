# Algoritmos - Guia de ML/DL

## Backpropagation

Algoritmo de treino que calcula gradientes e atualiza pesos.

### Forward Pass
```python
output = model(input)
loss = criterion(output, target)
```

### Backward Pass
```python
loss.backward()  # Calcula gradientes

optimizer.step()  # Atualiza pesos
optimizer.zero_grad()  # Zera gradientes
```

###链 de Derivação
```
Loss → Camada N → ... → Camada 1
```

## Activation Functions

### ReLU (mais usada)
```python
nn.ReLU()  # max(0, x)
```

### Sigmoid (binary)
```python
torch.sigmoid(x)  # 1/(1+e^-x)
```

### Softmax (multi-class)
```python
nn.Softmax(dim=1)(x)
```

### Tanh
```python
torch.tanh(x)  # (e^x - e^-x)/(e^x + e^-x)
```

## Loss Functions

### CrossEntropyLoss (classificação)
```python
criterion = nn.CrossEntropyLoss()
```

### MSELoss (regressão)
```python
criterion = nn.MSELoss()
```

### BCELoss (binária)
```python
criterion = nn.BCELoss()
```

## Optimizers

### Adam (default)
```python
torch.optim.Adam(model.parameters(), lr=0.001)
```

### SGD (momentum)
```python
torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
```

### AdamW (regularização)
```python
torch.optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
```

## Referências
[[tensor/gradients]]