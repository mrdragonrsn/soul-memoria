# Rede Neural Core - Guia

## O que é o Core
O núcleo computacional é onde os cálculos principais da rede neural acontecem. Contém os parâmetros treináveis (pesos e bias).

## Componentes

### Pesos (Weights)
- Matriz de conexão entre neurônios
- Atualizados durante treinamento via backpropagation
- shape: (camada_anterior, camada_atual)

### Bias
- Termo independente
- Deslocamento da ativação
- shape: (1, camada_atual)

### Sinapses
- Conexões entre neurônios
- Podem ter diferentes inicializações

## Como Inicializar

```python
import torch.nn as nn

# Xavier (tanh/sigmoid)
nn.init.xavier_uniform_(layer.weight)

# He (ReLU)
nn.init.kaiming_uniform_(layer.weight)

# Normal
nn.init.normal_(layer.weight, mean=0, std=0.01)
```

## Verificar Parâmetros
```python
for name, param in model.named_parameters():
    print(f"{name}: {param.shape}")
```

## Referências
[[algoritmos/backpropagation]]
[[redes/neural/weights]]