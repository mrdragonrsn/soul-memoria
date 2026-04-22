# GPU + CUDA - Guia

## Verificar GPU

```python
import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
print(torch.cuda.device_count())
```

## Device

```python
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
```

## Mover Dados

```python
X = X.to(device)
y = y.to(device)
```

## CUDA venv

### Criar ambiente virtual
```bash
python -m venv venv
source venv/Scripts/activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Memória GPU

```python
# Limpar cache
torch.cuda.empty_cache()

# Verificar uso
print(torch.cuda.memory_allocated() / 1024**3, "GB")
```

## Referências
[[tensor/index]]
[[algoritmos/index]]