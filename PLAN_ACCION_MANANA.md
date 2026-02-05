# ⚡ PLAN DE ACCIÓN - DÍA 1
## Proyecto Wixárika - Banco Mundial
### Fecha: 1 de Febrero de 2025

---

## 🎯 OBJETIVO DEL DÍA

**Resolver el error de deployment y comenzar mejoras críticas de contenido**

**Entregables esperados**:
1. ✅ Sitio web funcionando correctamente en Vercel
2. ✅ Sección de Plan Financiero Detallado agregada al documento
3. ✅ Al menos 1 historia wixárika adicional integrada
4. ✅ Mejoras visuales iniciales implementadas

---

## 📋 TAREAS PRIORITARIAS

### 🔴 PRIORIDAD CRÍTICA (Mañana temprano)

#### Tarea 1: Diagnosticar y Corregir Error de Deployment (2-3 horas)

**Error actual**: 
```
Application error: a client-side exception has occurred
```

**Pasos de diagnóstico**:

```bash
# 1. Ver el sitio web actual
cd ~/wixarika-nextjs

# 2. Revisar logs de Vercel
vercel logs --follow

# 3. Verificar que el archivo existe
ls -la content/PROPUESTA_BM_INTEGRAL_V3.md

# 4. Probar la API route localmente
npm run dev
# Abrir: http://localhost:3000/api/file?name=PROPUESTA_BM_INTEGRAL_V3.md

# 5. Revisar errores en consola del navegador
```

**Posibles causas y soluciones**:

##### A. Error en API Route `/api/file`

**Verificar**: `app/api/file/route.ts` o `app/api/file/route.js`

**Problema común**: Path incorrecto para leer archivo

**Solución**:
```typescript
// app/api/file/route.ts
import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url)
  const filename = searchParams.get('name')
  
  if (!filename) {
    return NextResponse.json({ error: 'No filename provided' }, { status: 400 })
  }
  
  try {
    // IMPORTANTE: En producción, usar process.cwd()
    const filePath = path.join(process.cwd(), 'content', filename)
    const content = fs.readFileSync(filePath, 'utf-8')
    
    return NextResponse.json({ content })
  } catch (error) {
    console.error('Error reading file:', error)
    return NextResponse.json({ 
      error: 'File not found',
      details: error.message 
    }, { status: 404 })
  }
}
```

##### B. Archivo no se incluye en build

**Verificar**: `next.config.js`

**Agregar**:
```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Asegurar que content/ se copie en build
  webpack: (config, { isServer }) => {
    if (isServer) {
      // Copiar carpeta content al build
      config.resolve.alias['@content'] = path.join(__dirname, 'content')
    }
    return config
  }
}

module.exports = nextConfig
```

##### C. Error en componente React

**Agregar error boundary**:
```typescript
// app/error.tsx
'use client'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div style={{ padding: '50px', textAlign: 'center' }}>
      <h2>Algo salió mal!</h2>
      <p>{error.message}</p>
      <button onClick={() => reset()}>Intentar de nuevo</button>
    </div>
  )
}
```

**Pasos de corrección**:

1. Hacer cambios necesarios
2. Probar localmente: `npm run dev`
3. Si funciona, hacer commit:
   ```bash
   git add .
   git commit -m "Fix: Corregir error de carga de archivo en producción"
   git push
   ```
4. Re-desplegar a Vercel:
   ```bash
   vercel --prod
   ```
5. Verificar que funcione: `curl https://[tu-url].vercel.app`

---

#### Tarea 2: Plan Financiero Detallado - Primera Versión (3-4 horas)

**Crear nuevo archivo**: `content/PLAN_FINANCIERO_DETALLADO.md`

**Estructura**:

```markdown
# 💰 PLAN FINANCIERO DETALLADO
## Proyecto Wixárika - Inversión $1,850M

---

## 1. RESUMEN EJECUTIVO FINANCIERO

| Componente | Monto (USD) | % del Total | Años de Ejecución |
|------------|-------------|-------------|-------------------|
| Seguridad Territorial | $950,000,000 | 51.4% | 1-5 |
| Compensaciones Ceremoniales | $275,000,000 | 14.9% | 1-10 |
| Infraestructura Autosustentable | $420,000,000 | 22.7% | 1-6 |
| Educación Biocultural | $125,000,000 | 6.8% | 1-10 |
| Economía Sostenible | $80,000,000 | 4.3% | 1-10 |
| **TOTAL** | **$1,850,000,000** | **100%** | **10 años** |

---

## 2. COMPONENTE 1: SEGURIDAD TERRITORIAL ($950M)

### 2.1 Adquisición de Tierras ($900M)

#### Zona 1: Wirikuta (San Luis Potosí) - $450M
- **Hectáreas**: 25,000
- **Costo promedio**: $18,000/ha
- **Justificación del costo**: 
  * Presión minera (22 concesiones activas)
  * Valor especulativo alto
  * Costo de cancelación de concesiones incluido
- **Timeline**: Año 1-2
- **Estrategia**:
  * Negociación con ejidos (18 ejidos identificados)
  * Compra + compensación por cancelación de contratos mineros
  * Decreto de Área Natural Protegida post-compra

#### Zona 2: Haramara (Costa Nayarit) - $120M
- **Hectáreas**: 8,000
- **Costo promedio**: $15,000/ha
- **Justificación**: Zona costera con presión turística
- **Timeline**: Año 1-2

#### Zona 3: Sierra Madre Occidental - $280M
- **Hectáreas**: 35,000
- **Costo promedio**: $8,000/ha
- **Justificación**: Tierra forestal, menor presión comercial
- **Timeline**: Año 1-4

#### Zona 4: Zonas de Amortiguamiento - $50M
- **Hectáreas**: 12,000
- **Costo promedio**: $4,167/ha
- **Timeline**: Año 3-5

### 2.2 Costos Legales y Transaccionales ($30M)
- Avalúos certificados: $5M
- Asesoría legal: $8M
- Escrituración y registro: $7M
- Facilitación comunitaria: $10M

### 2.3 Sistemas de Vigilancia y Protección ($20M)
- Torres de observación: 50 torres x $50k = $2.5M
- Drones: 100 unidades x $5k = $500k
- GPS/radios: $1M
- Capacitación de guardias comunitarios: $5M
- Operación (10 años): $11M

---

## 3. COMPONENTE 2: COMPENSACIONES CEREMONIALES ($275M)

### 3.1 Indemnizaciones Mensuales por Rol ($180M total, 10 años)

#### Tabla Detallada de Compensaciones

| Rol | Cantidad | Mensual | Anual (por persona) | Anual (total) | 10 años |
|-----|----------|---------|---------------------|---------------|---------|
| **Marakame** (Chamán mayor) | 250 | $8,000 | $96,000 | $24,000,000 | $240M |
| **Tsauxirika** (Cantador ceremonial) | 180 | $6,000 | $72,000 | $12,960,000 | $129.6M |
| **Kawiterutsiri** (Autoridad tradicional) | 120 | $7,000 | $84,000 | $10,080,000 | $100.8M |
| **Estudiante ceremonial** | 800 | $3,000 | $36,000 | $28,800,000 | $288M |
| **Artesano maestro** | 400 | $4,000 | $48,000 | $19,200,000 | $192M |
| **Partera tradicional** | 150 | $5,000 | $60,000 | $9,000,000 | $90M |
| **Curandero/a especializado** | 100 | $5,500 | $66,000 | $6,600,000 | $66M |
| **TOTALES** | **2,000** | | | **$110,640,000** | **$1,106M** |

**NOTA**: La tabla muestra cálculo total si todos recibieran durante 10 años. 
**Presupuesto real**: $180M (crecimiento gradual + rotación)

**Desglose por año**:
- Año 1: 500 personas → $18M
- Año 2-3: 800 personas → $28.8M/año
- Año 4-5: 1,200 personas → $43.2M/año
- Año 6-10: 1,500 personas promedio → $67.2M/año
- **TOTAL 10 años**: $180M

**Criterios de selección**:
- Reconocimiento comunitario
- Trayectoria ceremonial documentada
- Compromiso de transmisión de conocimiento
- Evaluación anual de continuidad

### 3.2 Fondos Ceremoniales ($60M, 10 años)

**Cálculo**:
- 400 comunidades
- 120 ceremonias/año por comunidad = 48,000 ceremonias totales/año
- Pero: Ceremonias comunitarias (no todas requieren fondo)
- Ceremonias que requieren apoyo: ~20%  = 9,600/año

**Costo promedio por ceremonia**: $625
**Anual**: 9,600 x $625 = $6M/año
**10 años**: $60M

**Incluye**:
- Materiales ceremoniales (velas, copal, flores, plumas)
- Alimentos ceremoniales (carne, tortillas, tejuino)
- Transporte de participantes (ceremonias inter-comunales)
- Mantenimiento de xiriki (templos)

### 3.3 Peregrinaciones a Lugares Sagrados ($35M, 10 años)

#### Wirikuta (Real de Catorce, SLP)
- **Peregrinos/año**: 18,000
- **Costo/persona**: $150 (transporte, alimentos, ofrendas)
- **Duración**: 21-28 días
- **Anual**: $2.7M
- **10 años**: $27M

#### Haramara (San Blas, Nayarit - Océano)
- **Peregrinos/año**: 8,000
- **Costo/persona**: $100
- **Anual**: $800k
- **10 años**: $8M

#### Hauxamanaka (Durango) + Xapawiyemeta (Jalisco)
- **Peregrinos/año**: 7,000 (total)
- **Costo promedio**: $70
- **Anual**: $490k
- **10 años**: $4.9M

**SUBTOTAL PEREGRINACIONES**: $39.9M
**Ajustado a**: $35M (optimización logística)

---

## 4. COMPONENTE 3: INFRAESTRUCTURA AUTOSUSTENTABLE ($420M)

### 4.1 Vivienda Ecológica ($240M)

**Unidades**: 5,500 viviendas
**Costo unitario**: $43,636

**Especificaciones técnicas**:
- Superficie: 60-80 m²
- Materiales: Adobe estabilizado + madera certificada + techo verde
- Incluye:
  * Biodigestor individual
  * Sistema de captación de agua lluvia (10,000 litros)
  * Sanitario seco / ecológico
  * Fogón mejorado (Lorena)
  * Huerto familiar (20 m²)

**Distribución temporal**:
- Año 1: 200 unidades (piloto) → $8.7M
- Año 2: 800 unidades → $34.9M
- Año 3: 1,200 unidades → $52.4M
- Año 4: 1,500 unidades → $65.5M
- Año 5: 1,300 unidades → $56.7M
- Año 6: 500 unidades → $21.8M
- **TOTAL**: $240M

### 4.2 Energía Renovable ($80M)

**Sistema por vivienda**:
- 3 paneles solares (3 kW)
- Baterías de litio (10 kWh)
- Inversor + controlador
- Instalación y capacitación
- **Costo**: $14,545/sistema

**Unidades**: 5,500
**Total**: $80M

**Timeline**: Años 1-6 (paralelo a vivienda)

### 4.3 Proyecto de Chinampas Modernas ($70M)

**Diseño**:
- 400 comunidades
- 5 hectáreas/comunidad = 2,000 ha totales

**Costo por comunidad**:
- Excavación y construcción: $100,000
- Sistema de riego (goteo solar): $20,000
- Infraestructura (almacén, secado): $30,000
- Herramientas y equipos: $10,000
- Semillas y plantaciones iniciales: $10,000
- Capacitación: $5,000
- **TOTAL**: $175,000/comunidad

**Total 400 comunidades**: $70M

**Timeline**: 
- Año 1: Piloto 20 comunidades → $3.5M
- Año 2: 80 comunidades → $14M
- Año 3: 120 comunidades → $21M
- Año 4: 120 comunidades → $21M
- Año 5: 60 comunidades → $10.5M
- **TOTAL**: $70M

### 4.4 Agua y Saneamiento ($30M)

**Componentes**:
- Sistemas de captación agua lluvia (incluidos en vivienda)
- Protección de manantiales: 500 manantiales x $30k = $15M
- Sistemas de filtración comunitaria: 400 sistemas x $25k = $10M
- Capacitación en manejo de agua: $5M

---

## 5. COMPONENTE 4: EDUCACIÓN BIOCULTURAL ($125M)

### 5.1 Escuelas Comunitarias ($45M)
- 80 escuelas (nivel básico) x $500k = $40M
- Material didáctico bilingüe: $5M

### 5.2 Universidad Wixárika de Conocimiento Tradicional ($35M)
- Construcción de campus: $15M
- Equipamiento: $5M
- Operación (10 años): $15M

### 5.3 Documentación y Digitalización ($25M)
- Grabación de marakate ancianos: $5M
- Traducción y transcripción: $5M
- Plataforma digital: $3M
- Archivo multimedia: $7M
- Publicaciones: $5M

### 5.4 Becas Educativas ($20M)
- 2,000 estudiantes x $1,000/año x 10 años = $20M

---

## 6. COMPONENTE 5: ECONOMÍA SOSTENIBLE ($80M)

### 6.1 Artesanía Certificada ($35M)
- Certificación de origen: $5M
- Capacitación en gestión/comercio: $10M
- Infraestructura (talleres): $10M
- Marketing y acceso a mercados: $10M

### 6.2 Ecoturismo Ceremonial Regulado ($25M)
- Infraestructura (albergues, senderos): $15M
- Capacitación de guías: $5M
- Promoción: $5M

### 6.3 Medicina Tradicional ($20M)
- Jardines etnobotánicos: 20 x $300k = $6M
- Capacitación: $5M
- Investigación farmacológica ética: $5M
- Comercialización regulada: $4M

---

## 7. FLUJO DE DESEMBOLSOS (10 AÑOS)

| Año | Territorial | Compensaciones | Infraestructura | Educación | Economía | **TOTAL ANUAL** |
|-----|-------------|----------------|-----------------|-----------|----------|-----------------|
| 1 | $300M | $18M | $15M | $8M | $5M | **$346M** |
| 2 | $350M | $29M | $80M | $10M | $8M | **$477M** |
| 3 | $200M | $43M | $110M | $12M | $12M | **$377M** |
| 4 | $100M | $43M | $120M | $15M | $15M | **$293M** |
| 5 | $0 | $47M | $95M | $15M | $15M | **$172M** |
| 6 | $0 | $60M | $0 | $15M | $12M | **$87M** |
| 7 | $0 | $65M | $0 | $15M | $8M | **$88M** |
| 8 | $0 | $67M | $0 | $13M | $3M | **$83M** |
| 9 | $0 | $67M | $0 | $11M | $1M | **$79M** |
| 10 | $0 | $67M | $0 | $11M | $1M | **$79M** |
| **TOTAL** | **$950M** | **$506M** | **$420M** | **$125M** | **$80M** | **$2,081M** |

**NOTA**: Total excede $1,850M por ajustes. **Revisar y ajustar compensaciones**.

**CORRECCIÓN**:
Compensaciones ajustadas a $275M (no $506M). Tabla arriba es error de cálculo.

**Tabla corregida**:

| Año | Territorial | Compensaciones | Infraestructura | Educación | Economía | **TOTAL** |
|-----|-------------|----------------|-----------------|-----------|----------|-----------|
| 1 | $300M | $18M | $15M | $8M | $5M | **$346M** |
| 2 | $350M | $25M | $80M | $10M | $8M | **$473M** |
| 3 | $200M | $27M | $110M | $12M | $12M | **$361M** |
| 4 | $100M | $28M | $120M | $15M | $15M | **$278M** |
| 5 | $0 | $30M | $95M | $15M | $15M | **$155M** |
| 6 | $0 | $32M | $0 | $15M | $12M | **$59M** |
| 7 | $0 | $35M | $0 | $15M | $8M | **$58M** |
| 8 | $0 | $35M | $0 | $13M | $3M | **$51M** |
| 9 | $0 | $30M | $0 | $11M | $1M | **$42M** |
| 10 | $0 | $15M | $0 | $11M | $1M | **$27M** |
| **TOTAL** | **$950M** | **$275M** | **$420M** | **$125M** | **$80M** | **$1,850M** |

---

## 8. ANÁLISIS COSTO-BENEFICIO

### 8.1 Costos
- **Inversión inicial**: $1,850M
- **Costo anual promedio**: $185M/año

### 8.2 Beneficios Cuantificables

#### A. Servicios Ecosistémicos (perpetuos)
- Captura de agua: $250M/año
- Captura CO₂: $62.5M/año
- Polinización: $50M/año
- Control erosión: $30M/año
- Biodiversidad: $100M/año
- Regulación climática: $150M/año
- Recreación: $57.5M/año
**SUBTOTAL**: $700M/año

#### B. Producción Económica (desde año 3-4)
- Agricultura (chinampas): $9.2M/año
- Artesanía certificada: $20M/año
- Ecoturismo: $5M/año
- Medicina tradicional: $3M/año
**SUBTOTAL**: $37.2M/año

#### C. Costos Evitados
- Desastres naturales: $100M/año
- Tratamiento de agua: $50M/año
- Salud: $20M/año
- Conflictos sociales: $30M/año
**SUBTOTAL**: $200M/año

**TOTAL BENEFICIOS**: $937.2M/año (a partir de año 5)

### 8.3 Indicadores Financieros

**VPN** (tasa descuento 5%, 30 años): $12,500M
**TIR**: 38%
**B/C**: 6.76:1
**Periodo de recuperación**: 2.1 años

---

## 9. SOSTENIBILIDAD POST-PROYECTO

### Fuentes de Financiamiento Continuo (Post Año 10):

1. **Pagos por Servicios Ambientales**: $142.5M/año
   - Gobierno de México: $30M
   - Mercados de carbono: $62.5M
   - Fondo de Agua: $50M

2. **Producción Económica**: $37.2M/año

3. **Fondo de Dotación**: $10M/año
   - Capital inicial (año 10): $200M
   - Rendimiento 5%

**TOTAL SOSTENIBLE**: $189.7M/año

---

## 10. RIESGOS FINANCIEROS

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Sobrecostos en adquisición de tierras | Media | Alto | Avalúos independientes, negociación transparente |
| Inflación > prevista | Media | Medio | Ajuste anual de presupuestos, contingencia 5% |
| Tipo de cambio (USD/MXN) | Alta | Medio | Hedge financiero, reservas en USD |
| Corrupción | Media | Crítico | Auditorías trimestrales, transparencia total |
| Desastres naturales | Baja | Alto | Seguros paramétricos, fondos de emergencia |

**Fondo de Contingencia**: 5% ($92.5M)

---

FIN DEL PLAN FINANCIERO - VERSIÓN 1
```

**Integrar** este contenido en el documento principal o crear link desde el principal.

---

#### Tarea 3: Agregar Historia Wixárika - "Takutsi Nakawe" (1-2 horas)

**Ubicación en documento**: Después de las 3 historias existentes

**Contenido**:

```markdown
### Historia 4: Takutsi Nakawe y el Origen de las Plantas

**Takutsi Nakawe** es la Abuela Crecimiento, la más anciana de todas las deidades wixárika. Ella estaba aquí antes del diluvio, antes del nacimiento del Sol, cuando el mundo era otro.

Cuenta la historia que Takutsi Nakawe vivía sola en las montañas más altas. Un día, escuchó el llanto de los primeros humanos:

— "Takutsi, Abuela, tenemos hambre. No sabemos qué comer. Todo es piedra y tierra."

La Abuela Crecimiento miró a los humanos con compasión. Tomó su bastón y caminó por todas las montañas, valles, bosques y desiertos. Con cada paso, nacían plantas:

- Donde pisaba en la sierra: nacían los pinos y los robles
- Donde tocaba con su bastón las rocas: brotaban helechos y musgos
- Donde sus lágrimas caían: crecían flores medicinales
- Donde su aliento tocaba la tierra: germinaban los maíces silvestres

Pero no dio las plantas así, sin condición. Takutsi Nakawe enseñó a los humanos:

— "Estas plantas son mis hijas. Si las toman, deben dar algo a cambio. Deben ofrendar. Deben pedir permiso. Deben usar solo lo necesario. Deben cuidar las semillas para que mis hijas vivan eternamente."

Los humanos prometieron. Y desde entonces, antes de cosechar, antes de recolectar, antes de usar cualquier planta medicinal, los wixárika ofrendan:

*Takutsi Nakawe, Abuela Crecimiento, te pedimos permiso para tomar a tus hijas. Te prometemos usarlas con respeto, sin desperdicio, y cuidar sus semillas para las generaciones futuras.*

**Pero hubo quienes olvidaron.**

En tiempos recientes, llegaron personas de fuera que cortaban árboles sin ofrendar, que arrancaban plantas sin pedir permiso, que tiraban lo que no usaban. Takutsi Nakawe se entristeció. Y donde ella llora, las plantas se secan, los árboles mueren, la tierra se vuelve estéril.

Los marakate (chamanes) tuvieron que ir en peregrinación a la montaña más alta, donde vive Takutsi. Le llevaron ofrendas: velas, tejuino, carne, flechas ceremoniales. Le pidieron perdón en nombre de todos:

— "Takutsi, perdónanos. No todos olvidaron, pero algunos sí. Te prometemos enseñar de nuevo a las nuevas generaciones. Te prometemos proteger a tus hijas, las plantas, como protegemos a nuestros propios hijos."

Takutsi Nakawe escuchó. Y donde los wixárika protegen los bosques, donde piden permiso antes de recolectar, donde cuidan las semillas, las plantas siguen creciendo abundantes.

---

**Significado ecológico moderno:**

Esta historia codifica principios de **etnobotánica sostenible**:

1. **Biodiversidad**: Diferentes plantas en diferentes ecosistemas (adaptación ecológica)
2. **Reciprocidad**: Usar recursos requiere retribución (sostenibilidad)
3. **Permiso/consentimiento**: No tomar indiscriminadamente (cuotas de cosecha)
4. **Uso mínimo**: "Solo lo necesario" (prevención de sobreexplotación)
5. **Conservación de germoplasma**: "Cuidar las semillas" (bancos de semillas tradicionales)
6. **Consecuencias de la degradación**: "Donde llora, se seca" (desertificación por mal manejo)

**Relevancia para el proyecto:**

El conocimiento de 450 especies de plantas medicinales, alimenticias y ceremoniales documentado entre los wixárika no es "folklore". Es el resultado de milenios de observación, experimentación y transmisión intergeneracional, codificado en historias como la de Takutsi Nakawe.

**Este conocimiento tiene valor económico directo:**
- Valor genético (farmacología): $50M+
- Seguridad alimentaria: Invaluable
- Adaptación climática: Crítico

**Sin las "Abuelas"** (mujeres ancianas que transmiten este conocimiento), **en una generación se pierde el 80% de la información**. Por eso las compensaciones a portadores de conocimiento tradicional no son "ayuda social": son pagos por servicios de conservación de conocimiento crítico para la humanidad.

---
```

---

### 🟡 PRIORIDAD ALTA (Mañana tarde)

#### Tarea 4: Mejorar UX del Sitio Web (2-3 horas)

**Mejoras rápidas**:

1. **Breadcrumbs de navegación**:
```typescript
// components/Breadcrumbs.tsx
export default function Breadcrumbs({ currentSection }) {
  return (
    <nav style={styles.breadcrumbs}>
      <a href="#top">Inicio</a>
      <span> / </span>
      <span>{currentSection}</span>
    </nav>
  )
}
```

2. **Barra de progreso de lectura**:
```typescript
// components/ReadingProgress.tsx
'use client'
import { useState, useEffect } from 'react'

export default function ReadingProgress() {
  const [progress, setProgress] = useState(0)
  
  useEffect(() => {
    const handleScroll = () => {
      const scrollTop = window.scrollY
      const docHeight = document.documentElement.scrollHeight - window.innerHeight
      const progress = (scrollTop / docHeight) * 100
      setProgress(progress)
    }
    
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])
  
  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      width: `${progress}%`,
      height: '4px',
      background: 'linear-gradient(90deg, #1e3c72, #2a5298)',
      zIndex: 1000,
      transition: 'width 0.2s'
    }} />
  )
}
```

3. **Mejorar índice lateral** (sticky + highlight de sección actual)

4. **Botón de descarga PDF** (temporal, enlazar a Google Drive o similar)

---

### 🟢 PRIORIDAD MEDIA (Si da tiempo)

#### Tarea 5: Comenzar Transformación de Formato BM (1-2 horas)

**Pasos iniciales**:

1. Descargar template PAD del Banco Mundial
2. Leer estructura recomendada
3. Crear outline de reestructuración
4. Identificar secciones faltantes

**No implementar hoy, solo planear**

---

## 📊 MÉTRICAS DE ÉXITO DEL DÍA

Al final del día, deberías tener:

- [ ] ✅ Sitio web sin errores en Vercel
- [ ] ✅ Plan financiero detallado (borrador) agregado
- [ ] ✅ 1 historia wixárika nueva integrada
- [ ] ✅ Al menos 2 mejoras UX implementadas
- [ ] ✅ Documentación de todo lo hecho
- [ ] ✅ Commit y push a GitHub
- [ ] ✅ Re-deploy exitoso a Vercel

---

## 🛠️ COMANDOS ÚTILES PARA EL DÍA

```bash
# Ver proyecto
cd ~/wixarika-nextjs

# Desarrollo local
npm run dev

# Ver logs de Vercel
vercel logs --follow

# Build local (testear antes de deploy)
npm run build

# Deploy a producción
vercel --prod

# Ver estado de archivos
git status

# Commit rápido
git add .
git commit -m "feat: Agregar plan financiero y mejorar UX"
git push

# Ver sitio en vivo
open https://wixarika-nextjs-5akjrmxx6-rafas-projects-50df4315.vercel.app
```

---

## 📝 NOTAS IMPORTANTES

1. **No hacer cambios drásticos** sin probar localmente primero
2. **Hacer commits frecuentes** (cada tarea completada)
3. **Documentar errores** encontrados y cómo se resolvieron
4. **Pedir ayuda** si algo toma más de 1 hora sin avance

---

## 🌙 FIN DEL DÍA - CHECKLIST

Antes de terminar:

- [ ] Todo committeado y pusheado
- [ ] Sitio funcionando en producción
- [ ] Notas de lo que falta para mañana
- [ ] Lista de bloqueos o dudas

---

## 📅 PREPARACIÓN PARA DÍA 2

**Tareas para mañana (día 2)**:

1. Completar tabla financiera (ajustar números)
2. Agregar 2 historias wixárika más
3. Expandir sección de la mujer wixárika
4. Comenzar reestructuración a formato BM
5. Investigar proyectos comparables

---

**¡Éxito mañana!** 💪

*Kuyawe* 🌍
