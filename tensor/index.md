# Tensor Operations - Guia

## Forward Pass
_PROPAGAÇÃO para Frente_

Executar a rede:

```python
def forward(x):
    x = self.conv1(x)
    x = F.relu(x)
    x = self.pool(x)
    return x
```

## Backward Pass
_PROPAGAÇÃO para Trás_

Retropropagar gradientes:

```python
loss.backward()
```

## Gradients

### Criar gradientes
```python
x = torch.randn(1, 10, requires_grad=True)
```

### Calcular gradiente
```python
loss.backward()
print(x.grad)  # gradiente de loss em relação a x
```

### Detach (remover do grafo)
```python
y = x.detach()  # não requer grad
```

### Clonar com grad
```python
y = x.clone()
y.requires_grad = True
```

## Operações Tensor

```python
#形状
x.shape  # torch.Size([batch, channels, H, W])

# Reshape
x = x.view(-1, 10)  # flatten

#permute (reordenar)
x = x.permute(0, 2, 3, 1)  # NCHW → NHWC
```

## Device (CPU/GPU)

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
x = x.to(device)
```

## Referências
[[algoritmos/index]]
[[gpu/cuda]]