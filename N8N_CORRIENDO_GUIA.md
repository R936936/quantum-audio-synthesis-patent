# 🎉 n8n CORRIENDO - GUÍA DE USO

## ✅ ESTADO ACTUAL

**n8n está corriendo exitosamente en tu Mac**

- **URL:** http://localhost:5678
- **Versión:** 1.118.2
- **Base de datos:** SQLite (~/.n8n/database.sqlite)
- **Encryption key:** Generada automáticamente
- **Status:** 🟢 Activo

---

## 🚀 ACCEDER A n8n

### Opción 1: Desde la terminal donde corre

```bash
# Presiona la tecla "o"
# Abre n8n automáticamente en el navegador
```

### Opción 2: Manualmente

```
Abrir navegador: http://localhost:5678
```

---

## 👤 PRIMERA VEZ: CREAR CUENTA

Cuando abras n8n por primera vez, te pedirá crear una cuenta:

```
Email: tu-email@example.com
First name: Tu Nombre
Last name: Apellido
Password: tu-contraseña-segura
```

**⚠️ IMPORTANTE:** 
- Todo es LOCAL (no se envía a ningún servidor)
- La cuenta es solo para ti
- Los datos se guardan en tu Mac

---

## 🎓 TUTORIAL INTEGRADO

n8n incluye un tutorial interactivo "Getting Started":

1. **Sigue las instrucciones** (5 minutos)
2. **Aprende los conceptos básicos:**
   - Nodes (nodos)
   - Connections (conexiones)
   - Workflows
   - Executions (ejecuciones)

---

## 🎯 TU PRIMER WORKFLOW

### Workflow Simple de Prueba

**Objetivo:** Probar integración con OpenAI

**Pasos:**

1. **Click "Add workflow"**
   - Nombre: "Test OpenAI"

2. **Agregar Manual Trigger:**
   - Click en "+" 
   - Buscar "Manual Trigger"
   - Click para agregar

3. **Agregar OpenAI node:**
   - Click en "+"
   - Buscar "OpenAI"
   - Seleccionar

4. **Configurar OpenAI:**
   - Resource: Chat
   - Operation: Message a model
   - Model: gpt-4
   - Messages → Text: "Escribe un haiku sobre programación"

5. **Conectar credentials:**
   - Click en "Credential to connect with"
   - "Create New Credential"
   - Name: "My OpenAI"
   - API Key: [pegar tu API key de OpenAI]
   - Save

6. **Conectar nodos:**
   - Arrastrar desde Manual Trigger → OpenAI

7. **Ejecutar:**
   - Click "Test workflow"
   - Ver resultado en OpenAI node

8. **Activar:**
   - Toggle "Active" → ON

---

## 🔑 TU API KEY DE OPENAI

Está guardada en:
```
~/vcv-rack-respell-automation/.env
```

Para verla:
```bash
cat ~/vcv-rack-respell-automation/.env | grep OPENAI_API_KEY
```

**Copiarla y pegarla** en las credentials de n8n.

---

## 📊 WORKFLOWS PARA VCV RACK

### Workflow 1: GitHub → Auto-Compile

**Trigger:** GitHub Push  
**Acción:** Compilar automáticamente

```
[GitHub Trigger]
    ↓
[HTTP Request] → POST localhost:3000/compile
    ↓
[If Node] → ¿Éxito?
    ├─ SÍ → [Discord] "✅ Build exitoso"
    └─ NO → [Discord] "❌ Build falló: {{logs}}"
```

---

### Workflow 2: Research Assistant

**Trigger:** Webhook  
**Acción:** Investigar tema DSP

```
[Webhook Trigger] → /research?topic=quantum
    ↓
[HTTP Request] → Google search
    ↓
[OpenAI] → Resume papers
    ↓
[OpenAI] → Genera código C++
    ↓
[GitHub] → Push a docs/
    ↓
[Discord] → Notificar
```

---

### Workflow 3: Documentation Auto-Update

**Trigger:** Cron (diario)  
**Acción:** Generar docs

```
[Cron Trigger] → 0 0 * * * (medianoche)
    ↓
[Execute Command] → find src/ -name "*.cpp"
    ↓
[Loop] → Por cada archivo
    ↓
[OpenAI] → Genera documentación
    ↓
[Aggregate] → Combina todo
    ↓
[GitHub] → Push docs/
    ↓
[Vercel] → Deploy website
```

---

## 🔌 CONECTAR MÁS SERVICIOS

### GitHub

1. Agregar "GitHub" node
2. Create credentials
3. OAuth2 o Personal Access Token
4. Autorizar

### Discord/Slack

1. Agregar "Discord" o "Slack" node
2. Create webhook URL en Discord/Slack
3. Pegar en n8n

### Notion

1. Agregar "Notion" node
2. Create integration en Notion
3. Conectar con n8n

---

## 💡 TIPS ÚTILES

### Debugging

- **Execution history:** Ve todas las ejecuciones
- **Error logs:** Click en nodo con error
- **Test mode:** Usa datos de prueba

### Organización

- **Carpetas:** Organiza workflows
- **Tags:** Etiqueta workflows
- **Notas:** Agrega notas a nodos

### Performance

- **Deactivate workflows** cuando no los uses
- **Clean execution data** periódicamente
- **Backup ~/.n8n/** regularmente

---

## 🔒 SEGURIDAD

### Credentials

Todas las credenciales están:
- **Encriptadas** en database.sqlite
- **Encryption key** en ~/.n8n/config
- **Backup ambos archivos** para no perder acceso

### API Keys

Al agregar API keys:
- Se guardan de forma segura
- No se ven en plain text
- Solo tú tienes acceso

---

## 📁 ESTRUCTURA DE ARCHIVOS

```
~/.n8n/
├── config                  ← Encryption key (BACKUP!)
├── database.sqlite         ← Workflows, credentials, executions
├── database.sqlite-wal     ← Write-ahead log
└── database.sqlite-shm     ← Shared memory

Backup recomendado:
   tar -czf n8n-backup-$(date +%Y%m%d).tar.gz ~/.n8n/
```

---

## ⚙️ CONFIGURACIÓN AVANZADA

### Variables de entorno

```bash
# Puerto (default: 5678)
export N8N_PORT=5678

# Timezone
export GENERIC_TIMEZONE=America/Mexico_City

# Webhook URL (para producción)
export WEBHOOK_URL=https://tu-dominio.com

# Security
export N8N_BLOCK_ENV_ACCESS_IN_NODE=true
```

### Ejecutar con config

```bash
N8N_PORT=8080 n8n start
```

---

## 🛑 DETENER n8n

### Desde terminal (donde corre):

```bash
# Presiona Ctrl+C
```

### Si corre con pm2:

```bash
pm2 stop n8n
pm2 delete n8n
```

---

## 🔄 REINICIAR n8n

### Terminal:

```bash
# Ctrl+C para detener
n8n start
```

### pm2:

```bash
pm2 restart n8n
```

---

## 📚 RECURSOS

### Documentación oficial:

- **Workflows:** https://docs.n8n.io/workflows/
- **Nodes:** https://docs.n8n.io/integrations/
- **Best practices:** https://docs.n8n.io/workflows/best-practices/

### Templates:

- **Galería:** https://n8n.io/workflows/
- Busca: "OpenAI", "GitHub", "automation"

### Comunidad:

- **Forum:** https://community.n8n.io
- **Discord:** n8n Discord
- **YouTube:** n8n tutorials

---

## 🎯 SIGUIENTES PASOS

### Hoy:
1. ✅ n8n corriendo (COMPLETADO)
2. ⏳ Abrir http://localhost:5678
3. ⏳ Crear cuenta
4. ⏳ Seguir tutorial
5. ⏳ Primer workflow con OpenAI

### Esta semana:
- Workflow: GitHub → Compile
- Workflow: Research DSP
- Workflow: Doc automation

### Próximas semanas:
- Pipeline CI/CD completo
- Community management
- Content automation

---

## ✅ CHECKLIST RÁPIDO

```
□ n8n corriendo en terminal
□ Abrir http://localhost:5678
□ Cuenta creada
□ Tutorial completado
□ OpenAI conectado
□ Primer workflow funcionando
□ Workflow activado
```

---

## 🚨 TROUBLESHOOTING

### "Port already in use"

```bash
# Ver qué usa el puerto
lsof -i :5678

# Usar otro puerto
export N8N_PORT=8080
n8n start
```

### "Cannot find module"

```bash
# Reinstalar n8n
npm uninstall -g n8n
npm install -g n8n
```

### "Database locked"

```bash
# Detener todas las instancias de n8n
pkill -f n8n

# Reiniciar
n8n start
```

---

## 💬 PREGUNTAS FRECUENTES

**¿Necesito internet?**
- Solo para conectar servicios externos (OpenAI, GitHub, etc.)
- n8n funciona local

**¿Los workflows corren 24/7?**
- Sí, mientras n8n esté corriendo
- Usa pm2 para que corra siempre

**¿Cuántos workflows puedo crear?**
- Ilimitados (self-hosted)

**¿Es gratis?**
- Sí, 100% gratis (self-hosted)
- n8n Cloud tiene costo

---

## 🎉 ¡LISTO!

**n8n está corriendo y listo para usar.**

**Próximo paso:**
1. Abrir http://localhost:5678
2. Crear cuenta
3. Crear primer workflow

**¡A automatizar todo!** 🚀

---

*Guía creada: Noviembre 8, 2025*  
*n8n Version: 1.118.2*  
*Status: 🟢 Running*
