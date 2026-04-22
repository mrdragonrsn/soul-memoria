# E:\IA - Memória Compartilhada para IAs

## Estrutura
```
E:\IA\
├── config/           # Configurações e preferências do usuário
│   └── obsidian.json
├── contexto/         # Sessão atual de trabalho
│   ├── sessao_atual.json
│   └── estado.md
├── memoria/         # Memória de longo prazo
│   ├── long_prazo.json
│   └── preferencias.md
├── historico/       # Histórico de sessões
│   └── sessoes.json
└── conhecimento/    # Base de conhecimento
    └── README.md
```

## Como usar
Para cada sessão, a IA deve:
1. Criar session_id único em `contexto/sessao_atual.json`
2. Salvar progresso em `contexto/estado.md` (visível no Obsidian)
3. Atualizar preferências em `memoria/long_prazo.json`
4. Registrar no `historico/sessoes.json`

---
*Criado: 2026-04-22 | Atualizado: 2026-04-22*