# 🤖 Agente Híbrido Especialista en Análisis y Levantamiento de Recursos para Proyectos

## 📋 Descripción

Este agente híbrido es una herramienta avanzada diseñada para realizar análisis exhaustivos de proyectos de software, identificando recursos, dependencias, tecnologías y proporcionando recomendaciones basadas en mejores prácticas.

### ✨ Características Principales

- **🔍 Análisis Automático de Estructura**: Escanea automáticamente todo el proyecto
- **🔧 Detección de Tecnologías**: Identifica lenguajes de programación y frameworks
- **📦 Análisis de Dependencias**: Extrae y analiza dependencias de múltiples ecosistemas
- **🎯 Identificación de Recursos**: Categoriza archivos por tipo y propósito
- **📊 Métricas del Proyecto**: Calcula estadísticas relevantes
- **💡 Recomendaciones Inteligentes**: Sugiere mejoras basadas en mejores prácticas
- **📝 Múltiples Formatos de Reporte**: Markdown, JSON, HTML

## 🚀 Instalación

### Requisitos

- Python 3.8 o superior
- Sistema operativo: Windows, macOS, Linux

### Instalación Simple

```bash
# Descargar el agente
wget https://example.com/project_resource_agent.py

# Dar permisos de ejecución (Unix/macOS)
chmod +x project_resource_agent.py

# Ejecutar
python3 project_resource_agent.py /ruta/al/proyecto
```

### Instalación con Dependencias Opcionales

```bash
pip install -r requirements_agent.txt
```

## 💻 Uso

### Uso Básico

```bash
# Analizar el directorio actual
python3 project_resource_agent.py

# Analizar un proyecto específico
python3 project_resource_agent.py /ruta/al/proyecto

# Generar reporte en Markdown (por defecto)
python3 project_resource_agent.py /ruta/al/proyecto --format markdown
```

### Formatos de Salida

```bash
# Reporte en JSON
python3 project_resource_agent.py . --format json --output reporte.json

# Reporte en HTML
python3 project_resource_agent.py . --format html --output reporte.html

# Reporte en Markdown
python3 project_resource_agent.py . --format markdown --output ANALISIS.md
```

### Opciones Avanzadas

```bash
# Ver ayuda completa
python3 project_resource_agent.py --help

# Desactivar colores
python3 project_resource_agent.py . --no-color
```

## 📊 Capacidades de Análisis

### Tecnologías Soportadas

El agente detecta automáticamente:

- **Python**: `.py`, `requirements.txt`, `setup.py`, `pyproject.toml`
- **JavaScript/TypeScript**: `.js`, `.jsx`, `.ts`, `.tsx`, `package.json`
- **Java**: `.java`, `pom.xml`, `build.gradle`
- **Go**: `.go`, `go.mod`, `go.sum`
- **Rust**: `.rs`, `Cargo.toml`
- **PHP**: `.php`, `composer.json`
- **Ruby**: `.rb`, `Gemfile`
- **C#**: `.cs`, `.csproj`, `.sln`
- **Docker**: `Dockerfile`, `docker-compose.yml`
- **Kubernetes**: `.yaml`, `.yml` (configuraciones k8s)
- **Terraform**: `.tf`, archivos de estado
- **Ansible**: playbooks y configuraciones

### Análisis de Dependencias

- **Python**: `requirements.txt`, `pyproject.toml`, `Pipfile`
- **Node.js**: `package.json` (dependencies y devDependencies)
- **Java**: `pom.xml`, `build.gradle`
- **Go**: `go.mod`
- **Rust**: `Cargo.toml`
- **PHP**: `composer.json`
- **Ruby**: `Gemfile`

### Categorización de Recursos

- **Código Fuente**: Archivos de código principal
- **Configuración**: Archivos de configuración del proyecto
- **Documentación**: README, CHANGELOG, docs
- **Tests**: Archivos de pruebas
- **Base de Datos**: Scripts SQL, migraciones
- **Archivos Estáticos**: CSS, HTML, assets
- **Media**: Imágenes, videos, audio
- **Datos**: JSON, YAML, CSV, XML

## 📈 Ejemplo de Salida

### Consola

```
🔍 Analizando proyecto: mi-proyecto
📁 Ruta: /Users/usuario/mi-proyecto

📊 Fase 1: Escaneando archivos...
   ✓ 342 archivos encontrados (15.43 MB)

🔧 Fase 2: Detectando tecnologías...
   ✓ Tecnologías detectadas: docker, javascript, python, typescript

📦 Fase 3: Analizando dependencias...
   ✓ 47 dependencias encontradas

🎯 Fase 4: Identificando recursos clave...
   ✓ 89 recursos clave identificados

📈 Fase 5: Calculando métricas...
   ✓ Métricas calculadas

💡 Fase 6: Generando recomendaciones...
   ✓ 5 recomendaciones generadas
```

### Reporte Markdown

```markdown
# 📊 Análisis de Recursos del Proyecto: mi-proyecto

**Fecha de análisis:** 2024-01-15T10:30:00
**Ruta del proyecto:** `/Users/usuario/mi-proyecto`

## 📈 Resumen Ejecutivo

- **Total de archivos:** 342
- **Tamaño total:** 15.43 MB
- **Tecnologías detectadas:** 4
- **Grupos de dependencias:** 3
- **Recursos clave identificados:** 89

## 🔧 Tecnologías Detectadas

- **Docker**
- **Javascript**
- **Python**
- **Typescript**

...
```

## 🎯 Casos de Uso

### 1. Auditoría de Proyectos

Realizar auditorías rápidas de proyectos heredados o nuevos:

```bash
python3 project_resource_agent.py /proyecto-legacy --format html --output auditoria.html
```

### 2. Documentación Automática

Generar documentación inicial de estructura del proyecto:

```bash
python3 project_resource_agent.py . --format markdown --output ESTRUCTURA.md
```

### 3. Evaluación de Recursos

Evaluar recursos necesarios para migración o refactorización:

```bash
python3 project_resource_agent.py /proyecto --format json --output recursos.json
```

### 4. Análisis de Dependencias

Identificar dependencias obsoletas o problemas de seguridad:

```bash
python3 project_resource_agent.py . > analisis-dependencias.txt
```

### 5. Onboarding de Desarrolladores

Proporcionar vista general del proyecto a nuevos miembros del equipo:

```bash
python3 project_resource_agent.py /proyecto --format html --output onboarding.html
```

## 🔧 Personalización

### Extender Patrones de Tecnologías

Puedes modificar el diccionario `TECH_PATTERNS` en el código para agregar nuevas tecnologías:

```python
TECH_PATTERNS = {
    'mi_tecnologia': ['.ext', 'config-file.txt'],
    # ...
}
```

### Agregar Nuevas Categorías de Recursos

Modifica el diccionario `resource_categories` en el método `_identify_resources`:

```python
resource_categories = {
    'mi_categoria': ['.myext', 'pattern'],
    # ...
}
```

### Personalizar Recomendaciones

Edita el método `_generate_recommendations` para agregar lógica personalizada.

## 📚 API Programática

Puedes usar el agente como módulo de Python:

```python
from project_resource_agent import ProjectResourceAgent

# Crear instancia del agente
agent = ProjectResourceAgent('/ruta/al/proyecto')

# Ejecutar análisis
analysis = agent.analyze()

# Acceder a resultados
print(f"Tecnologías: {analysis.technologies}")
print(f"Total de archivos: {analysis.file_count}")
print(f"Dependencias: {len(analysis.dependencies)}")

# Generar reporte
report = agent.generate_report(analysis, format='markdown')
print(report)
```

### Estructura de Datos

```python
@dataclass
class ProjectAnalysis:
    project_name: str
    root_path: str
    timestamp: str
    resources: List[Resource]
    technologies: List[str]
    dependencies: Dict[str, List[str]]
    file_count: int
    total_size: int
    recommendations: List[str]
    metrics: Dict[str, Any]
```

## 🛡️ Mejores Prácticas

1. **Ejecutar en repositorios limpios**: Asegúrate de que `node_modules`, `venv`, etc. estén excluidos
2. **Revisar recomendaciones**: Las recomendaciones son sugerencias, no requisitos absolutos
3. **Complementar con otras herramientas**: Este agente es complementario a herramientas de CI/CD
4. **Mantener actualizado**: Revisa periódicamente las tecnologías soportadas

## ⚡ Rendimiento

- **Proyectos pequeños** (<1000 archivos): < 5 segundos
- **Proyectos medianos** (1000-10000 archivos): 5-30 segundos
- **Proyectos grandes** (>10000 archivos): 30-120 segundos

El agente excluye automáticamente directorios pesados como:
- `node_modules`
- `.git`
- `venv`, `env`, `.venv`
- `__pycache__`
- `dist`, `build`, `target`
- `.idea`, `.vscode`

## 🐛 Solución de Problemas

### Error: "No se detectaron tecnologías"

- Verifica que los archivos de configuración estén en el directorio raíz
- El agente busca patrones específicos de archivos

### Error: "Permission denied"

- Asegúrate de tener permisos de lectura en el directorio
- En Unix/macOS, usa `chmod +x` si es necesario

### Reporte muy grande

- Usa formato JSON para análisis programático
- Los reportes HTML y Markdown limitan automáticamente el contenido

## 🤝 Contribuciones

Este agente puede ser extendido fácilmente. Algunas ideas:

- [ ] Análisis de complejidad ciclomática
- [ ] Integración con APIs de GitHub/GitLab
- [ ] Detección de problemas de seguridad
- [ ] Análisis de código duplicado
- [ ] Generación de diagramas de arquitectura
- [ ] Estimación de esfuerzos de desarrollo
- [ ] Análisis de licencias de dependencias

## 📄 Licencia

Este agente es de código abierto y puede ser usado libremente para proyectos personales y comerciales.

## 🔗 Enlaces Útiles

- [Documentación de Python](https://docs.python.org/)
- [Mejores prácticas de estructura de proyectos](https://github.com/topics/project-structure)
- [Guías de documentación](https://www.writethedocs.org/)

## 📞 Soporte

Para reportar problemas o sugerir mejoras:

1. Revisa la documentación
2. Busca en issues existentes
3. Crea un nuevo issue con detalles específicos

---

**Creado con ❤️ para facilitar el análisis y documentación de proyectos de software**
