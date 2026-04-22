# Redes Neurais - Guia Completo

## Visão Geral
Redes neurais artificiais são sistemas computacionais inspirados no cérebro humano, compostos por camadas de neurônios artificiais que processam informações.

## Estrutura Básica
```
Entrada → Camada Oculta → Camada Oculta → ... → Saída
```

## Tipos de Arquitetura

### Redes Feedforward
- Dados fluem em uma direção
- Sem ciclos
- Exemplos: MLP, Dense

### Redes Recorrentes (RNN)
- Processam sequências
- Memória de estados anteriores
- Exemplos: LSTM, GRU

### Redes Convolucionais (CNN)
- Extraem features espaciais
- Ideal para imagens
- Exemplo: Conv2D, Pooling

### Transformers
- Atenção automática
- Base de LLMs modernos
- Encoder-Decoder

## Como Usar

### 1. Definir Arquitetura
```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(input_size, hidden),
    nn.ReLU(),
    nn.Linear(hidden, output)
)
```

### 2. Treinar
```python
optimizer = torch.optim.Adam(model.parameters())
loss_fn = nn.CrossEntropyLoss()

for epoch in range(epochs):
    for batch in dataloader:
        optimizer.zero_grad()
        output = model(batch)
        loss = loss_fn(output, labels)
        loss.backward()
        optimizer.step()
```

### 3. Inferir
```python
model.eval()
with torch.no_grad():
    prediction = model(input_tensor)
```

## Referências
[[algoritmos/backpropagation]]
[[algoritmos/activation]]
[[tensor/forward]]