# ✅ n8n INSTALADO - PRÓXIMOS PASOS

## 🎉 INSTALACIÓN EXITOSA

n8n se instaló correctamente en tu sistema.

**Detalles:**
- Paquetes instalados: 1,960
- Tiempo de instalación: ~1 minuto
- Versión: 1.118.2 (última estable)

---

## 🚀 CÓMO INICIAR n8n

### Opción 1: Inicio Simple (Recomendado para empezar)

```bash
n8n start
```

Esto:
- Iniciará n8n en tu terminal
- Se abrirá automáticamente en: http://localhost:5678
- Los logs aparecerán en la terminal
- Ctrl+C para detener

---

### Opción 2: Background con pm2 (Recomendado para producción)

```bash
# 1. Instalar pm2
npm install -g pm2

# 2. Iniciar n8n como servicio
pm2 start n8n

# 3. Ver status
pm2 status

# 4. Ver logs
pm2 logs n8n

# 5. Detener
pm2 stop n8n

# 6. Reiniciar
pm2 restart n8n

# 7. Configurar auto-start al reiniciar Mac
pm2 startup
pm2 save
```

Esto:
- Corre n8n en background
- Se reinicia automáticamente si se cae
- Sobrevive reinicios del sistema
- No necesitas dejar terminal abierta

---

## 📋 PRIMER USO

Cuando inicies n8n por primera vez:

1. **Se abre automáticamente** en http://localhost:5678
2. **Crear cuenta:** 
   - Email: tu email
   - Password: tu contraseña
   - (Todo es local, no se envía a ningún servidor)
3. **Tutorial integrado:** Sigue el "Getting Started"
4. **Crear primer workflow**

---

## 🎯 WORKFLOWS SUGERIDOS PARA EMPEZAR

### 1. Workflow de Prueba Simple

```
Webhook Trigger → OpenAI Node → HTTP Response
```

**Para qué:** Probar la integración con OpenAI

**Cómo crear:**
1. Click "Add workflow"
2. Agregar "Webhook" node
3. Agregar "OpenAI" node
4. Conectar API key de OpenAI
5. Agregar "Respond to Webhook" node
6. Ejecutar test

---

### 2. GitHub → Compilación → Notificación

```
GitHub Trigger → HTTP Request (compile) → Discord/Slack
```

**Para qué:** Auto-compilación cuando haces push

**Necesitas:**
- Webhook de GitHub configurado
- Endpoint de compilación (localhost:3000/compile)
- Discord/Slack webhook

---

### 3. Research Assistant

```
Webhook → Google Search → OpenAI → Notion
```

**Para qué:** Investigación automática de temas DSP

---

## 🔑 CONECTAR OPENAI A n8n

Cuando crees un workflow con OpenAI:

1. Agregar nodo "OpenAI"
2. Click en "Credentials"
3. "Create New"
4. Pegar tu API key: `sk-...`
5. Save

**Tu API key actual ya está en `.env`**
Puedes reutilizarla para n8n.

---

## 📚 RECURSOS

### Documentación:
- Oficial: https://docs.n8n.io
- Workflows: https://docs.n8n.io/workflows/
- Nodes: https://docs.n8n.io/integrations/

### Templates:
- Galería: https://n8n.io/workflows/
- Busca: "OpenAI", "GitHub", "automation"

### Comunidad:
- Forum: https://community.n8n.io
- Discord: n8n Discord server

---

## ⚙️ CONFIGURACIÓN

### Archivo de configuración

n8n guarda datos en: `~/.n8n/`

```bash
~/.n8n/
├── config/          # Configuración
├── database.sqlite  # Base de datos (workflows)
└── credentials.json # Credenciales encriptadas
```

### Variables de entorno

Puedes configurar n8n con variables:

```bash
# Puerto (default: 5678)
export N8N_PORT=5678

# Host
export N8N_HOST=localhost

# Timezone
export GENERIC_TIMEZONE=America/Mexico_City

# Webhook URL (para producción)
export WEBHOOK_URL=https://tu-dominio.com

# Iniciar con config
n8n start
```

---

## 🔒 SEGURIDAD

### Credenciales

- Todas las credenciales se almacenan **encriptadas**
- Encryption key en: `~/.n8n/config`
- **Importante:** Hacer backup de `~/.n8n/config`

### API Keys

Cuando agregues API keys a n8n:
- OpenAI
- GitHub
- Discord/Slack
- Etc.

Todas se guardan de forma segura.

---

## 🎓 TUTORIAL RÁPIDO

### Crear tu primer workflow (5 minutos)

1. **Iniciar n8n:**
   ```bash
   n8n start
   ```

2. **Abrir navegador:** http://localhost:5678

3. **Crear workflow:**
   - Click "Add workflow"
   - Nombre: "Test OpenAI"

4. **Agregar Webhook node:**
   - Click "+"
   - Buscar "Webhook"
   - Method: GET
   - Path: test

5. **Agregar OpenAI node:**
   - Click "+"
   - Buscar "OpenAI"
   - Operation: "Message a model"
   - Model: gpt-4
   - Prompt: "Say hello in Spanish"

6. **Conectar credentials:**
   - En OpenAI node → Credentials
   - "Create New"
   - API Key: tu key de OpenAI

7. **Ejecutar:**
   - Click "Test workflow"
   - Ver resultado

8. **Activar:**
   - Toggle "Active" en ON
   - Webhook ahora está live

---

## 🚨 TROUBLESHOOTING

### n8n no inicia

```bash
# Ver qué está usando el puerto 5678
lsof -i :5678

# Usar otro puerto
export N8N_PORT=5679
n8n start
```

### Olvidé la contraseña

```bash
# Reset owner account
n8n user-management:reset
```

### Limpiar todo y empezar fresh

```bash
# Backup primero
mv ~/.n8n ~/.n8n.backup

# Iniciar fresh
n8n start
```

---

## 📊 MONITOREO

### Ver workflows activos

Desde la UI de n8n:
- Dashboard muestra workflows activos
- Execution history
- Error logs

### Logs en terminal

```bash
# Si corriendo directo
n8n start
# Los logs aparecen en tiempo real

# Si corriendo con pm2
pm2 logs n8n
pm2 logs n8n --lines 100
```

---

## 🎯 SIGUIENTES PASOS

### Hoy:
1. ✅ Instalar n8n (COMPLETADO)
2. ⏳ Iniciar n8n: `n8n start`
3. ⏳ Crear primer workflow de prueba
4. ⏳ Conectar OpenAI

### Esta semana:
- Workflow: GitHub → Compile
- Workflow: Research assistant
- Workflow: Doc generator

### Próximas semanas:
- Pipeline CI/CD completo
- Community management
- Content automation

---

## 💡 TIPS

1. **Empieza simple:** Workflow de prueba con 2-3 nodos
2. **Usa templates:** Copia workflows de la galería
3. **Test frecuente:** Ejecuta workflows antes de activar
4. **Backup:** `~/.n8n/` contiene todo
5. **Documentar:** Agrega notas a tus workflows

---

## ✅ CHECKLIST

```
□ n8n instalado
□ n8n iniciado
□ Cuenta creada
□ Tutorial "Getting Started" completado
□ Primer workflow de prueba creado
□ OpenAI conectado
□ Workflow activado
```

---

**¡Ahora ejecuta: `n8n start` y empieza a crear workflows!** 🚀

---

*Guía creada: Noviembre 8, 2025*  
*Para: VCV Rack Development Automation*
