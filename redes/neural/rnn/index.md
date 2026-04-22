# RNN - Redes Neurais Recorrentes

## O que são RNNs
Processam dados sequenciais mantendo "memória" do que veio antes.

##tipos

### LSTM (Long Short-Term Memory)
```
Célula LSTM:
- Forget Gate: O que esquecer?
- Input Gate: O que adicionar?
- Output Gate: O que mostrar?
```

```python
import torch.nn as nn

lstm = nn.LSTM(
    input_size=256,
    hidden_size=512,
    num_layers=2,
    batch_first=True,
    dropout=0.1,
    bidirectional=True
)
```

### GRU (Gated Recurrent Unit)
Mais simples que LSTM, mais rápido.

```python
gru = nn.GRU(
    input_size=256,
    hidden_size=512,
    num_layers=2,
    batch_first=True
)
```

## Sequência de Entrada
```python
# shape: (batch, seq_len, features)
input_seq = torch.randn(32, 10, 256)

output, (h_n, c_n) = lstm(input_seq)
```

## Quando Usar
- Texto/Sequências → LSTM/GRU
- Previsão de séries temporais
- Tradução

## Referências
[[nlp/index]]
[[algoritmos/activation]]