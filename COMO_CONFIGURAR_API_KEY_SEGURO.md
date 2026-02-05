# 🔒 CÓMO CONFIGURAR API KEY DE FORMA SEGURA

## ⚠️ LO QUE PASÓ

Compartiste tu API key públicamente. Esto es peligroso porque:
- Cualquiera puede usarla
- Pueden gastar tu crédito
- Queda en historial de conversación

## ✅ SOLUCIÓN (3 pasos)

### Paso 1: REVOCAR la key comprometida (2 min)

1. Ir a: https://platform.openai.com/api-keys
2. Buscar la key que compartiste (sk-proj-rGen6...)
3. Click en los 3 puntos "..." 
4. Click en "Revoke"
5. Confirmar revocación

✅ Key antigua revocada = Ya no puede usarse

---

### Paso 2: CREAR nueva key (2 min)

1. En la misma página: https://platform.openai.com/api-keys
2. Click en "Create new secret key"
3. Nombre: "VCV Rack Automation - Private"
4. **⚠️ COPIAR la key (se muestra solo una vez)**
5. **⚠️ NO COMPARTIR con nadie (ni en chat)**

---

### Paso 3: CONFIGURAR de forma SEGURA (3 min)

**Opción A: Desde terminal (RECOMENDADO)**

```bash
# 1. Ir al proyecto
cd ~/vcv-rack-respell-automation

# 2. Editar .env de forma segura
nano .env

# 3. Dentro del editor, agregar:
OPENAI_API_KEY=pega_tu_nueva_key_aqui

# 4. Guardar:
# Presiona: Ctrl+X
# Presiona: Y (yes)
# Presiona: Enter
```

**Opción B: Con script interactivo (MÁS SEGURO)**

```bash
# Este script te pedirá la key de forma segura
cd ~/vcv-rack-respell-automation

# Ejecutar:
read -s -p "Pega tu OpenAI API key: " OPENAI_KEY
echo ""
echo "OPENAI_API_KEY=$OPENAI_KEY" > .env
echo "✅ Key configurada de forma segura"
unset OPENAI_KEY

# La key NO se muestra en pantalla
# NO queda en historial del shell
```

---

## 🔒 REGLAS DE ORO PARA API KEYS

### ❌ NUNCA hagas esto:

1. **NO compartir keys en chats** (público o privado)
2. **NO hacer commit a git** (.env está en .gitignore)
3. **NO ponerlas en código fuente**
4. **NO compartirlas en screenshots**
5. **NO enviarlas por email**

### ✅ SIEMPRE haz esto:

1. **Guardar en archivos .env** (están en .gitignore)
2. **Usar variables de entorno**
3. **Revocar keys comprometidas inmediatamente**
4. **Usar keys diferentes por proyecto**
5. **Revisar uso regularmente** (platform.openai.com/usage)

---

## 🛡️ VERIFICACIÓN DE SEGURIDAD

Después de configurar, verifica:

```bash
# 1. Verificar que .env NO está en git
cd ~/vcv-rack-respell-automation
git status .env
# Debe decir: "Untracked" o no aparecer

# 2. Verificar que .env tiene la key
cat .env | grep OPENAI_API_KEY
# Debe mostrar: OPENAI_API_KEY=sk-...
# (tu key nueva, diferente a la anterior)

# 3. Verificar que .gitignore protege .env
cat .gitignore | grep .env
# Debe mostrar: .env

# 4. Test de integración (sin exponer key)
python3 scripts/openai_integration.py test
# Debe pasar ✅
```

---

## 🔄 SI LA KEY SE COMPROMETE OTRA VEZ

1. **Revocar inmediatamente** en platform.openai.com
2. **Crear nueva key**
3. **Actualizar .env**
4. **Investigar cómo se expuso**
5. **Revisar commits en git** (git log --all -- .env)

---

## 💰 MONITOREO DE SEGURIDAD

### Configurar alertas de gasto

1. Ir a: https://platform.openai.com/account/billing/limits
2. Establecer límite mensual (ej: $20)
3. Activar alertas por email
4. Revisar uso semanalmente

### Revisar uso

```bash
# Ver uso actual
open https://platform.openai.com/usage
```

Si ves uso que no reconoces = Key comprometida

---

## ✅ CHECKLIST DE SEGURIDAD

Antes de continuar, verifica:

- [ ] Key antigua revocada
- [ ] Nueva key creada
- [ ] .env configurado
- [ ] .env NO en git
- [ ] Test de integración pasa
- [ ] Límites de gasto configurados
- [ ] **NUNCA más compartir keys públicamente**

---

## 🚀 DESPUÉS DE CONFIGURAR

Ejecuta:

```bash
cd ~/vcv-rack-respell-automation
python3 scripts/openai_integration.py test
```

Si pasa ✅ = Todo configurado correctamente y de forma segura

---

## 📚 RECURSOS

- **OpenAI Best Practices:** https://platform.openai.com/docs/guides/safety-best-practices
- **API Key Management:** https://platform.openai.com/api-keys
- **Usage Dashboard:** https://platform.openai.com/usage

---

**"Las API keys son como llaves de tu casa: nunca las compartas."** 🔒

---

*Creado: Noviembre 8, 2025*  
*Urgencia: 🔴 CRÍTICA*
