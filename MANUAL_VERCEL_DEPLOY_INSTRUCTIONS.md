# 📚 Manual Aurum Lab - Deploy en Vercel

## ✅ Proyecto Creado

**Ubicación:** `~/aurum-modules-manual/`

**Módulos documentados:**
- 🕐 **Fibonacci Clock** (6 HP, 3 canales BPM)
- ⚡ **Golden Trigger** (18 HP, 27 triggers con ratio áureo)

---

## 🚀 Cómo Deployar en Vercel

### Opción 1: Deploy Directo (MÁS RÁPIDO)

```bash
# 1. Instalar Vercel CLI globalmente
npm install -g vercel

# 2. Ir al proyecto
cd ~/aurum-modules-manual

# 3. Instalar dependencias
npm install

# 4. Deploy a Vercel
vercel
```

**Durante el deploy te preguntará:**
- Setup and deploy? → **Y**
- Which scope? → Elige tu cuenta
- Link to existing project? → **N**
- Project name → **aurum-lab-manual** (o el que quieras)
- Directory → **./** (presiona Enter)
- Override settings? → **N**

Vercel te dará una URL como: `https://aurum-lab-manual.vercel.app`

---

### Opción 2: Deploy desde GitHub

```bash
# 1. Crear repositorio en GitHub (opcional)
cd ~/aurum-modules-manual
git init
git add .
git commit -m "Initial commit: Aurum Lab manual"
git remote add origin https://github.com/TU_USUARIO/aurum-lab-manual.git
git push -u origin main

# 2. En vercel.com:
# - Click "New Project"
# - Importa tu repositorio de GitHub
# - Vercel auto-detecta Next.js
# - Click "Deploy"
```

---

## 🎨 Características del Manual

### Página Principal (`/`)
- Card de Fibonacci Clock
- Card de Golden Trigger
- Links de navegación
- Footer con φ = 1.618...

### Fibonacci Clock (`/fibonacci-clock`)
- Overview del módulo
- Controles detallados (knobs, displays, outputs)
- Layout del panel
- Casos de uso
- Especificaciones técnicas
- Tips & tricks

### Golden Trigger (`/golden-trigger`)
- Explicación del ratio áureo (φ)
- Controles por canal (clock, CV, knobs)
- Sistema de outputs 3×3
- Control global φ WIDTH
- Casos de uso
- Especificaciones técnicas
- Tips & tricks

---

## 🔧 Desarrollo Local

```bash
cd ~/aurum-modules-manual
npm install
npm run dev
```

Abre: `http://localhost:3000`

**Hot reload:** Los cambios se ven instantáneamente.

---

## 📝 Editar el Manual

### Estructura de archivos:

```
aurum-modules-manual/
├── app/
│   ├── page.tsx                    # Página principal
│   ├── fibonacci-clock/page.tsx    # Manual Fibonacci Clock
│   ├── golden-trigger/page.tsx     # Manual Golden Trigger
│   └── globals.css                 # Estilos globales
```

### Para añadir contenido:

1. Edita el archivo `.tsx` correspondiente
2. Guarda
3. El navegador se actualiza automáticamente (dev mode)
4. Cuando estés listo: `vercel --prod` para actualizar

---

## 🎨 Personalización

### Colores:

El manual usa los colores de Aurum Lab:
- **Dorado:** `#FFD700` (`.text-aurum-gold`)
- **Oscuro:** `#1a1a1a` (`.bg-aurum-dark`)

Definidos en: `tailwind.config.ts` y `globals.css`

### Agregar nueva página:

```bash
mkdir app/nueva-pagina
touch app/nueva-pagina/page.tsx
```

---

## ✅ Checklist de Deploy

- [ ] Proyecto creado en `~/aurum-modules-manual/`
- [ ] `npm install` ejecutado
- [ ] `npm run dev` funciona localmente
- [ ] Vercel CLI instalado (`npm i -g vercel`)
- [ ] Deploy ejecutado (`vercel`)
- [ ] URL de producción recibida
- [ ] Manual accesible en internet

---

## 📊 URLs del Proyecto

Una vez deployado:

- **Home:** `https://aurum-lab-manual.vercel.app/`
- **Fibonacci Clock:** `https://aurum-lab-manual.vercel.app/fibonacci-clock`
- **Golden Trigger:** `https://aurum-lab-manual.vercel.app/golden-trigger`

---

## 🆘 Troubleshooting

### Error: "Module not found"
```bash
cd ~/aurum-modules-manual
rm -rf node_modules package-lock.json
npm install
```

### Error durante build
```bash
npm run build
# Revisa los errores en consola
```

### Actualizar deploy
```bash
cd ~/aurum-modules-manual
vercel --prod
```

---

## 📚 Recursos

- [Vercel Docs](https://vercel.com/docs)
- [Next.js Docs](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)

---

**¡Manual listo para deploy! 🚀**

El proyecto está completo y listo para subir a Vercel.
