# Manual de Sincronização - Git

## Regra Importante
**NUNCA** criar arquivos `.txt`. Sempre usar extensão `.md` (Markdown).

## Regra Principal
**SEMPRE** que atualizar qualquer arquivo de memória, sincronizar com Git.

## Quando Sincronizar
- Após modificar `memoria/preferencias.md`
- Após modificar `memoria/long_prazo.json`
- Após modificar `contexto/estado.md`
- Após modificar `contexto/sessao_atual.json`
- Após criar/atualizar qualquer arquivo em `E:\IA\`

## Comandos
```bash
cd E:\IA
git add .
git commit -m "Atualização: [descrição breve]"
git push
```

## Regra Importante
**NUNCA** criar arquivos `.txt`. Sempre usar extensão `.md` (Markdown).

## Fluxo Completo
1. Ler estado atual: `git status`
2. Atualizar arquivos necessários
3. Adicionar: `git add .`
4. Commit: `git commit -m "update: [o que foi feito]"`
5. Push: `git push`

## Alias Recomendado
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

_Regra activada: 2026-04-23_