# Manuais de Operação Técnica

## 1. BlackMamba (C2) 🐍🛡️

### Arquitetura
- Bypass AMSI antes de carregar payload
- Ofuscação de tráfego HTTPS simulado
- Evitar EDR/AV em tempo real

### Operacional
- Nunca compilar com PyInstaller padrão (usar Nuitka)
- Gerar crypt_key dinamicamente por campanha
- Persistência: HKCU\Run ou tarefas agendadas

---

## 2. PKM (Obsidian + Git) 🧠📖

### Arquitetura
- Estratégia de merge automática
- Excluir .obsidian/ do Git

### Operacional
- .gitignore com .obsidian/workspace
- Daemon: agendador a cada 30min
- Fallback: log em caso de erro de rede

---

## 3. Jarvis (TTS) 🎙️🤖

### Arquitetura
- Fallback: ElevenLabs → pyttsx3/Edge-TTS

### Operacional
- API Key em .env (nunca no código)
- try/except para erro 401/Timeout
- Limpar cache de áudio após pygame

---

## 4. Telog (Infraestrutura) 🌐🏢

### Operacional
- Scripts PowerShell para diagnóstico
- Nmap para varredura de rede
- Documentar incidentes no Obsidian

---

## 5. Magisk Root 📱🔓

### Operacional
- Zygisk + DenyList para apps bancários
- Módulos: Systemless Hosts
- Backup: stock boot.img para recuperação

---

## 6. Yamaha R15 🏍️⚡

### Operacional
- SpeedoHealer após mudança de relação
- Lavar/lubrificar filtro DNA a cada 5.000km
- Telemetria GPS para aferição real

---

_Atualizado: 2026-04-22_