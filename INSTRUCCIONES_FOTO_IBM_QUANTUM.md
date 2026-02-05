# 📸 INSTRUCCIONES: CÓMO AGREGAR FOTO REAL DEL HARDWARE IBM QUANTUM

## 🎯 Objetivo

Insertar una fotografía oficial del hardware IBM Quantum (procesador Heron R2 / sistema ibm_fez) en el **CERTIFICADO_WAVETABLE_CUANTICO_V2.md** antes de convertirlo a PDF.

---

## 📁 DÓNDE CONSEGUIR LAS FOTOS OFICIALES

### ✅ Fuentes Oficiales de IBM:

1. **IBM Quantum Media Center**
   ```
   https://newsroom.ibm.com/media-quantum-innovation?keywords=quantum&l=100
   ```
   - Galería oficial con imágenes de alta resolución
   - Fotos del refrigerador de dilución
   - Procesadores Heron montados
   - Crédito: Connie Zhou / IBM Quantum

2. **IBM Newsroom - Image Gallery**
   ```
   https://newsroom.ibm.com/media-center
   ```
   - Buscar: "quantum computer" o "heron processor"
   - Imágenes HD descargables

3. **IBM Quantum Hardware Page**
   ```
   https://www.ibm.com/quantum/hardware
   ```
   - Ilustraciones técnicas
   - Fotos de los sistemas Quantum

---

## 🖼️ TIPOS DE FOTOS RECOMENDADAS

### Opción 1: **Refrigerador de Dilución Completo** (RECOMENDADO)
- **Qué buscar:** Cilindro dorado/plateado criogénico
- **Descripción:** "Dilution refrigerator housing IBM Quantum Heron processor"
- **Visual:** Sistema completo donde se aloja el procesador ibm_fez
- **Impacto:** Muestra la escala y complejidad del hardware real

**Ejemplo de búsqueda:**
```
"IBM Quantum dilution refrigerator Heron"
```

### Opción 2: **Procesador Heron R2 Montado**
- **Qué buscar:** Chip superconductor en circuito dorado
- **Descripción:** "IBM Heron R2 processor mounted on circuit board"
- **Visual:** Close-up del chip de 156 qubits
- **Impacto:** Muestra el cerebro cuántico real

**Ejemplo de búsqueda:**
```
"IBM Heron processor chip 156 qubits"
```

### Opción 3: **Sistema en Laboratorio IBM**
- **Qué buscar:** Vista del lab con múltiples sistemas cuánticos
- **Descripción:** "IBM Quantum Lab with multiple quantum systems"
- **Visual:** Contexto profesional de investigación
- **Impacto:** Muestra la infraestructura real

---

## 📝 CÓMO INSERTAR LA FOTO EN EL CERTIFICADO

### Paso 1: **Descargar la Imagen**

En tu navegador, ve a una de las fuentes oficiales de arriba y:

```bash
# Guarda la imagen descargada como:
~/ibm_quantum_hardware.jpg
# O
~/ibm_quantum_hardware.png
```

**Requisitos de la imagen:**
- Formato: JPG o PNG
- Resolución mínima: 1200×800 px
- Tamaño recomendado: 2-5 MB
- Aspecto: Horizontal (landscape) preferido

---

### Paso 2: **Abrir el Certificado en un Editor**

#### Opción A - Usar Markdown con Preview (macOS):

```bash
# 1. Abrir el certificado en editor
open -a "Typora" ~/CERTIFICADO_WAVETABLE_CUANTICO_V2.md
# O usar cualquier editor Markdown (Typora, MacDown, VSCode)

# 2. Buscar esta línea (Página 1):
[FOTO: IBM QUANTUM HERON R2 PROCESSOR]

# 3. Reemplazar con:
![IBM Quantum Heron R2 Hardware](./ibm_quantum_hardware.jpg)
```

#### Opción B - Usar Pandoc (conversión directa):

```bash
# Insertar imagen con Pandoc sintaxis
![IBM Quantum ibm_fez Hardware - Refrigerador criogénico del procesador Heron R2 (156 qubits superconductores). Temperatura: ~15 millikelvin. Crédito: Connie Zhou / IBM Quantum](./ibm_quantum_hardware.jpg){ width=90% }
```

---

### Paso 3: **Convertir a PDF con la Imagen Embebida**

#### Opción A - Pandoc (RECOMENDADO):

```bash
cd ~

# Conversión con imagen embebida
pandoc CERTIFICADO_WAVETABLE_CUANTICO_V2.md \
  -o CERTIFICADO_WAVETABLE_CUANTICO_V2.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=10pt \
  --resource-path=.:~/

# Verificar que se generó
ls -lh CERTIFICADO_WAVETABLE_CUANTICO_V2.pdf
```

#### Opción B - Editor con Exportación (Typora, MacDown):

1. Abre `CERTIFICADO_WAVETABLE_CUANTICO_V2.md` en Typora
2. File → Export → PDF
3. Asegúrate de que "Include Images" esté ✅
4. Export

#### Opción C - Página por Página (Para control fino):

```bash
# Convertir solo página 1 primero para verificar imagen
head -200 CERTIFICADO_WAVETABLE_CUANTICO_V2.md | \
  pandoc -o test_page1.pdf --pdf-engine=xelatex
  
# Revisar test_page1.pdf para verificar que la imagen se ve bien
open test_page1.pdf

# Si se ve bien, convertir todo
pandoc CERTIFICADO_WAVETABLE_CUANTICO_V2.md -o CERTIFICADO_FINAL.pdf
```

---

## 🎨 AJUSTAR TAMAÑO DE LA FOTO

Si la foto sale muy grande o muy pequeña en el PDF:

### En Markdown:

```markdown
<!-- Tamaño específico en pulgadas (para imprimir en Letter) -->
![Hardware IBM Quantum](./ibm_quantum_hardware.jpg){ width=5in }

<!-- O en porcentaje de ancho de página -->
![Hardware IBM Quantum](./ibm_quantum_hardware.jpg){ width=70% }
```

### En HTML (si el editor lo soporta):

```html
<img src="./ibm_quantum_hardware.jpg" 
     alt="IBM Quantum ibm_fez Hardware" 
     width="600px" 
     style="display: block; margin: 20px auto;" />
```

---

## ✅ VERIFICACIÓN FINAL

Antes de imprimir, verifica que el PDF tenga:

- [ ] Foto del hardware IBM Quantum visible en **Página 1**
- [ ] Imagen con resolución clara (no pixelada)
- [ ] Crédito fotográfico: "Connie Zhou / IBM Quantum" visible
- [ ] Código QR embebido en **Página 2** (2.5" × 2.5")
- [ ] Código QR grande en **Página 5** (3.5" × 3.5")
- [ ] Total: 5 páginas completas
- [ ] Márgenes correctos (1 pulgada en todos los lados)

```bash
# Ver info del PDF generado
pdfinfo CERTIFICADO_WAVETABLE_CUANTICO_V2.pdf

# Debería mostrar:
# Pages: 5
# Page size: 612 x 792 pts (letter)
```

---

## 🖨️ IMPRESIÓN PROFESIONAL

### Especificaciones Recomendadas:

| Aspecto | Especificación |
|---------|----------------|
| **Papel** | Bond blanco 24 lb (90 g/m²) |
| **Tamaño** | Letter (8.5" × 11") |
| **Impresión** | Color (para foto y QR) |
| **Resolución** | 300 DPI mínimo |
| **Acabado** | Mate (evitar brillante para QR) |
| **Enmarcado** | Marco 8.5"×11" con vidrio UV |

### Proveedores Sugeridos:

- **FedEx Office / Kinko's** - Impresión certificada
- **Staples** - Papel certificado disponible
- **Impresoras locales** - Para papel especial (lino/pergamino)

---

## 🌐 EJEMPLOS DE FOTOS OFICIALES IBM

### Foto Tipo 1: Refrigerador de Dilución

**Descripción ideal para el certificado:**
```
IBM Quantum Heron R2 Dilution Refrigerator
Sistema ibm_fez - 156 Qubits Superconductores
Temperatura operativa: ~15 millikelvin (-273.135°C)
Crédito: Connie Zhou / IBM Quantum
```

### Foto Tipo 2: Procesador Heron R2

**Descripción ideal para el certificado:**
```
IBM Heron R2 Quantum Processor (156 qubits)
Chip superconductor montado en placa criogénica
El cerebro del sistema ibm_fez
Crédito: IBM Quantum
```

---

## 📱 INSERTAR EL CÓDIGO QR

Ya tienes el QR generado: `~/QUANTUM_QR_CODE.png`

### En Página 2 del certificado:

```markdown
## PÁGINA 2 - Código QR de Verificación

![Quantum Job QR Code](./QUANTUM_QR_CODE.png){ width=2.5in }

**Job ID:** d5lt7gt9j2ac739k64q0  
**URL:** https://quantum.ibm.com/jobs/d5lt7gt9j2ac739k64q0
```

### En Página 5 del certificado:

```markdown
## PÁGINA 5 - Código QR Grande

![Quantum Job QR Code](./QUANTUM_QR_CODE.png){ width=3.5in }
```

---

## 🚀 SCRIPT AUTOMATIZADO (TODO-EN-UNO)

Guarda esto como `~/generar_certificado_completo.sh`:

```bash
#!/bin/bash

echo "🌌 Generando Certificado Cuántico Completo..."

# 1. Verificar que existen los recursos
if [ ! -f ~/QUANTUM_QR_CODE.png ]; then
    echo "❌ Falta: QUANTUM_QR_CODE.png"
    exit 1
fi

if [ ! -f ~/ibm_quantum_hardware.jpg ]; then
    echo "⚠️  Advertencia: No se encontró ibm_quantum_hardware.jpg"
    echo "   Descarga una foto de: https://newsroom.ibm.com/media-quantum-innovation"
    echo ""
    echo "¿Continuar sin la foto? (y/N)"
    read -r respuesta
    if [[ ! "$respuesta" =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# 2. Convertir Markdown → PDF
echo "📄 Convirtiendo a PDF..."
pandoc ~/CERTIFICADO_WAVETABLE_CUANTICO_V2.md \
    -o ~/CERTIFICADO_WAVETABLE_CUANTICO_FINAL.pdf \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=10pt \
    -V documentclass=article \
    --resource-path=.:~/

# 3. Verificar resultado
if [ -f ~/CERTIFICADO_WAVETABLE_CUANTICO_FINAL.pdf ]; then
    echo "✅ Certificado generado exitosamente!"
    echo ""
    echo "📄 Archivo: ~/CERTIFICADO_WAVETABLE_CUANTICO_FINAL.pdf"
    
    # Mostrar info
    pdfinfo ~/CERTIFICADO_WAVETABLE_CUANTICO_FINAL.pdf | grep -E "Pages|Page size"
    
    # Abrir para revisar
    echo ""
    echo "🔍 Abriendo para revisión..."
    open ~/CERTIFICADO_WAVETABLE_CUANTICO_FINAL.pdf
else
    echo "❌ Error al generar PDF"
    exit 1
fi

echo ""
echo "🖨️  Listo para imprimir!"
echo "   Papel: Bond blanco 24 lb"
echo "   Tamaño: Letter (8.5\" × 11\")"
echo "   Color: Sí (para foto y QR)"
```

### Uso:

```bash
chmod +x ~/generar_certificado_completo.sh
~/generar_certificado_completo.sh
```

---

## 💡 TIPS PRO

### 1. **Foto con transparencia (si tienes Photoshop/GIMP):**

```bash
# Remover fondo de la foto para look más profesional
convert ibm_quantum_hardware.jpg \
    -fuzz 10% -transparent white \
    ibm_quantum_hardware_clean.png
```

### 2. **Añadir borde sutil a la foto:**

```markdown
![IBM Quantum Hardware](./ibm_quantum_hardware.jpg){ width=5in style="border: 1px solid #ccc; padding: 10px;" }
```

### 3. **Crear versión imprimible vs digital:**

```bash
# Versión digital (menor tamaño, para email)
pandoc CERTIFICADO_WAVETABLE_CUANTICO_V2.md \
    -o CERTIFICADO_DIGITAL.pdf \
    --pdf-engine=xelatex \
    -V geometry:margin=0.75in

# Versión imprimible (alta calidad)
pandoc CERTIFICADO_WAVETABLE_CUANTICO_V2.md \
    -o CERTIFICADO_IMPRESION.pdf \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    --dpi=300
```

---

## 📧 COMPARTIR EL CERTIFICADO

### Digitalmente:

```bash
# Optimizar para email (reducir tamaño)
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
   -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH \
   -sOutputFile=CERTIFICADO_EMAIL.pdf \
   CERTIFICADO_WAVETABLE_CUANTICO_FINAL.pdf

# Resultado: ~1-2 MB en lugar de ~5-10 MB
```

### Web (Portfolio/LinkedIn):

1. Sube a Google Drive / Dropbox
2. Genera link público
3. O sube a GitHub repo como asset
4. Comparte el link en bio/portfolio

---

## 🏆 RESULTADO FINAL

Tu certificado debería verse así:

```
╔═══════════════════════════════════════════════╗
║  🌌 CERTIFICADO DE WAVETABLE CUÁNTICO 🌌     ║
║                                               ║
║  [FOTO REAL DEL HARDWARE IBM QUANTUM]         ║
║  Refrigerador criogénico @ 15 mK              ║
║                                               ║
║  Backend: ibm_fez (156 qubits)                ║
║  Job ID: d5lt7gt9j2ac739k64q0                 ║
║  Timestamp: 16 Enero 2025                     ║
║                                               ║
║  [CÓDIGO QR - Página 2]                       ║
║  Escaneable, verificable                      ║
║                                               ║
║  ✅ Hardware real                             ║
║  ✅ Superposición cuántica                    ║
║  ✅ Entrelazamiento genuino                   ║
║  ✅ Único en el universo                      ║
║                                               ║
║  5 páginas totales                            ║
╚═══════════════════════════════════════════════╝
```

---

## ✅ CHECKLIST FINAL

Antes de considerar el certificado completo:

- [ ] Foto del hardware IBM descargada y guardada
- [ ] Foto insertada en el certificado (Página 1)
- [ ] Crédito fotográfico incluido ("Connie Zhou / IBM")
- [ ] QR code embebido en Página 2
- [ ] QR code grande en Página 5
- [ ] Convertido a PDF con todas las imágenes
- [ ] PDF tiene exactamente 5 páginas
- [ ] QR codes escaneables desde el PDF
- [ ] Foto se ve clara (no pixelada)
- [ ] Texto legible en todas las secciones
- [ ] Márgenes correctos para impresión Letter

---

## 🆘 TROUBLESHOOTING

### Problema: "Pandoc no encuentra la imagen"

**Solución:**
```bash
# Usar ruta absoluta
pandoc ~/CERTIFICADO_WAVETABLE_CUANTICO_V2.md \
  -o ~/certificado.pdf \
  --resource-path=/Users/wu/
```

### Problema: "Imagen muy grande en PDF"

**Solución:** Edita el markdown y ajusta:
```markdown
![Hardware](./ibm_quantum_hardware.jpg){ width=4in }
```

### Problema: "QR no escanea desde el PDF"

**Solución:**
1. Verificar resolución del QR: mínimo 500×500 px
2. Aumentar DPI: `--dpi=300` en pandoc
3. Usar PDF viewer con zoom antes de escanear

### Problema: "Pandoc no instalado"

**Solución:**
```bash
brew install pandoc
brew install --cask basictex  # Para xelatex
```

---

## 🌌 FIN DE LAS INSTRUCCIONES

¡Ahora tienes todo lo necesario para crear un certificado profesional completo con foto real del hardware IBM Quantum!

**Resultado:** Certificado de 5 páginas, con foto verificable del hardware ibm_fez, QR codes escaneables, y toda la información técnica completa.

---

📧 Preguntas? → GitHub Issues o documentación en el repo
🌐 Fuentes: https://newsroom.ibm.com/media-quantum-innovation
