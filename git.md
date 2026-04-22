# Git - Configuração

## Repositório Remoto
- **URL**: https://github.com/mrdragonrsn/soul-memoria
- **Branch**: master

## Como Atualizar
```bash
cd E:\IA
git add .
git commit -m "Descrição da atualização"
git push
```

## Alias (PowerShell)
Adicionar ao PowerShell profile:
```powershell
function Push-Soul {
    cd E:\IA
    git add .
    git commit -m $args[0]
    git push
}
```

---

_Repositório criado: 2026-04-22_