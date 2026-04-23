# Transformer - Arquitetura

## O que é Transformer
Usa "Self-Attention" para processar sequências inteiras em paralelo. Base de GPT, BERT, Llama.

## Componentes

### Attention (Mecanismo de Atenção)
```python
import torch.nn as nn

attention = nn.MultiheadAttention(
    embed_dim=512,
    num_heads=8,
    dropout=0.1
)

# Query, Key, Value
Q = torch.randn(32, 10, 512)
K = torch.randn(32, 10, 512)
V = torch.randn(32, 10, 512)

output, attn_weights = attention(Q, K, V)
```

### Encoder
- Processa entrada
- Self-attention bidirecional
- BERT usa só encoder

### Decoder
- Gera saída
- Masked attention
- GPT usa só decoder

## Arquitetura Completa
```python
from transformers import TransformerEncoder, TransformerEncoderLayer

encoder_layer = nn.TransformerEncoderLayer(
    d_model=512,
    nhead=8,
    dim_feedforward=2048
)

transformer = TransformerEncoder(
    encoder_layer,
    num_layers=6
)
```

## Modelos Populares
- GPT (Decoder-only)
- BERT (Encoder)
- T5 (Encoder-Decoder)
- Llama (Decoder)

## Referências
[[nlp/llm]]
[[transformer/attention]]