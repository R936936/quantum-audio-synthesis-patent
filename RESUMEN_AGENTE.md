# 🤖 Agente Híbrido Especialista en Análisis y Levantamiento de Recursos

## 📦 Archivos Incluidos

1. **`project_resource_agent.py`** - Agente principal (código completo)
2. **`demo_agent.py`** - Script de demostración interactiva
3. **`advanced_usage_example.py`** - Ejemplos de uso avanzado
4. **`README_AGENT.md`** - Documentación completa
5. **`GUIA_RAPIDA.md`** - Guía de inicio rápido
6. **`CI_CD_TEMPLATES.md`** - Plantillas de integración CI/CD
7. **`requirements_agent.txt`** - Dependencias opcionales
8. **`RESUMEN_AGENTE.md`** - Este archivo

## 🚀 Inicio Inmediato

### Opción 1: Demo Rápida (Recomendado para empezar)

```bash
python3 demo_agent.py
```

Esto creará un proyecto de ejemplo y ejecutará un análisis completo mostrando todas las capacidades.

### Opción 2: Analizar Tu Proyecto

```bash
# Análisis básico
python3 project_resource_agent.py /ruta/a/tu/proyecto

# Con reporte HTML
python3 project_resource_agent.py . --format html --output analisis.html
```

### Opción 3: Ejemplos Avanzados

```bash
python3 advanced_usage_example.py
```

## ✨ Características Principales

### 1. Análisis Automático
- ✅ Escaneo completo de estructura del proyecto
- ✅ Detección automática de tecnologías
- ✅ Análisis de dependencias (Python, Node.js, Java, Go, Rust, etc.)
- ✅ Categorización inteligente de recursos
- ✅ Cálculo de métricas relevantes

### 2. Generación de Reportes
- 📝 **Markdown** - Para documentación y README
- 🔧 **JSON** - Para integración con herramientas
- 🌐 **HTML** - Para visualización en navegador

### 3. Recomendaciones Inteligentes
- 💡 Basadas en mejores prácticas de la industria
- 🎯 Específicas para tu proyecto
- 📊 Priorizadas por impacto

### 4. Múltiples Casos de Uso
- 🔍 Auditoría de proyectos
- 📚 Documentación automática
- 💪 Evaluación de recursos
- 🏥 Monitoreo de salud del proyecto
- 👥 Onboarding de desarrolladores
- 🚀 Integración CI/CD

## 🔧 Tecnologías Soportadas

| Lenguaje/Framework | Archivos Detectados | Análisis de Dependencias |
|-------------------|---------------------|--------------------------|
| Python | `.py`, `requirements.txt`, `pyproject.toml` | ✅ |
| JavaScript/Node.js | `.js`, `.jsx`, `package.json` | ✅ |
| TypeScript | `.ts`, `.tsx`, `tsconfig.json` | ✅ |
| Java | `.java`, `pom.xml`, `build.gradle` | ✅ |
| Go | `.go`, `go.mod` | ✅ |
| Rust | `.rs`, `Cargo.toml` | ✅ |
| PHP | `.php`, `composer.json` | ✅ |
| Ruby | `.rb`, `Gemfile` | ✅ |
| C# | `.cs`, `.csproj`, `.sln` | ✅ |
| Docker | `Dockerfile`, `docker-compose.yml` | ✅ |
| Kubernetes | `.yaml`, `.yml` (configs k8s) | ✅ |
| Terraform | `.tf`, archivos de estado | ✅ |
| Ansible | playbooks, `ansible.cfg` | ✅ |

## 📊 Ejemplo de Salida

### En Consola
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

✨ ¡Análisis completado!
```

### Reporte JSON (Extracto)
```json
{
  "project_name": "mi-proyecto",
  "file_count": 342,
  "total_size": 16180224,
  "technologies": ["docker", "javascript", "python", "typescript"],
  "dependencies": {
    "requirements.txt": ["flask==2.3.0", "pytest==7.3.1"],
    "npm dependencies": ["react@^18.2.0", "axios@^1.4.0"]
  },
  "metrics": {
    "total_size_human": "15.43 MB",
    "code_files": 127,
    "config_files": 15,
    "doc_files": 8
  },
  "recommendations": [
    "🧪 Se recomienda implementar tests automatizados",
    "🚀 Considerar implementar CI/CD"
  ]
}
```

## 🎯 Casos de Uso Reales

### 1. Auditoría Rápida de Proyecto Legacy
```bash
python3 project_resource_agent.py /proyecto-legacy \
  --format html \
  --output auditoria_$(date +%Y%m%d).html
```

### 2. Documentación para Nuevo Miembro del Equipo
```bash
python3 project_resource_agent.py . \
  --format markdown \
  --output docs/ESTRUCTURA_PROYECTO.md
```

### 3. Análisis Pre-deployment
```bash
python3 project_resource_agent.py . \
  --format json \
  --output pre_deploy_analysis.json
```

### 4. Reporte Semanal Automático
```bash
# En crontab
0 9 * * 1 cd /proyecto && python3 project_resource_agent.py . \
  -f html -o reports/weekly_$(date +\%Y\%m\%d).html
```

### 5. Integración en Pipeline CI/CD
Ver archivo `CI_CD_TEMPLATES.md` para ejemplos completos de:
- GitHub Actions
- GitLab CI
- Jenkins
- CircleCI
- Azure Pipelines
- Travis CI
- Bitbucket Pipelines

## 💻 Uso Programático

### Python API

```python
from project_resource_agent import ProjectResourceAgent

# Crear instancia y analizar
agent = ProjectResourceAgent('/ruta/al/proyecto')
analysis = agent.analyze()

# Acceder a resultados
print(f"Proyecto: {analysis.project_name}")
print(f"Archivos: {analysis.file_count}")
print(f"Tecnologías: {', '.join(analysis.technologies)}")
print(f"Tamaño: {analysis.metrics['total_size_human']}")

# Generar reportes
markdown_report = agent.generate_report(analysis, 'markdown')
json_report = agent.generate_report(analysis, 'json')
html_report = agent.generate_report(analysis, 'html')

# Filtrar recursos específicos
code_files = [r for r in analysis.resources if r.type == 'source_code']
config_files = [r for r in analysis.resources if r.type == 'configuration']

# Analizar dependencias
for dep_file, deps in analysis.dependencies.items():
    print(f"\n{dep_file}:")
    for dep in deps:
        print(f"  - {dep}")
```

### Análisis Comparativo (Ejemplo Avanzado)

```python
from advanced_usage_example import AdvancedAnalyzer

# Comparar múltiples proyectos
analyzer = AdvancedAnalyzer()
projects = ['/proyecto1', '/proyecto2', '/proyecto3']
analyzer.analyze_projects(projects)

# Generar reporte comparativo
comparison = analyzer.generate_comparison_report()
print(f"Salud promedio: {comparison['summary']['average_health_score']}/100")

# Calcular score de salud individual
for analysis in analyzer.analyses:
    health = analyzer.calculate_health_score(analysis)
    print(f"{analysis.project_name}: {health['score']}/100 - {health['grade']}")
```

## 📚 Estructura de Datos

### Resource (Recurso Individual)
```python
@dataclass
class Resource:
    name: str              # Nombre del archivo
    type: str              # Tipo: source_code, configuration, documentation, etc.
    path: str              # Ruta relativa
    size: Optional[int]    # Tamaño en bytes
    description: str       # Descripción del recurso
    dependencies: List[str] # Dependencias del recurso
```

### ProjectAnalysis (Análisis Completo)
```python
@dataclass
class ProjectAnalysis:
    project_name: str                    # Nombre del proyecto
    root_path: str                       # Ruta raíz
    timestamp: str                       # Timestamp ISO 8601
    resources: List[Resource]            # Lista de recursos
    technologies: List[str]              # Tecnologías detectadas
    dependencies: Dict[str, List[str]]   # Dependencias por archivo
    file_count: int                      # Total de archivos
    total_size: int                      # Tamaño total en bytes
    recommendations: List[str]           # Recomendaciones
    metrics: Dict[str, Any]              # Métricas calculadas
```

## 🛠️ Personalización

### Agregar Nueva Tecnología

Edita `project_resource_agent.py`:

```python
TECH_PATTERNS = {
    # ...existentes...
    'mi_tecnologia': ['.ext', 'config-file.txt', 'special.conf'],
}
```

### Personalizar Exclusiones

```python
exclude_dirs = {
    '.git', '__pycache__', 'node_modules', 'venv',
    # Añade tus exclusiones
    'mis_archivos_temp',
    'directorio_a_ignorar'
}
```

### Agregar Recomendaciones Personalizadas

Modifica el método `_generate_recommendations()`:

```python
def _generate_recommendations(self) -> List[str]:
    recommendations = []
    
    # Tus reglas personalizadas
    if self.file_count > 5000:
        recommendations.append("📦 Proyecto muy grande, considerar modularizar")
    
    # ...resto de recomendaciones...
    return recommendations
```

## 🔍 Métricas Calculadas

El agente calcula automáticamente:

- **total_files**: Número total de archivos
- **total_size_bytes**: Tamaño en bytes
- **total_size_human**: Tamaño legible (KB, MB, GB)
- **technologies_count**: Número de tecnologías detectadas
- **dependency_groups**: Grupos de dependencias
- **resource_categories**: Conteo por categoría
- **code_files**: Archivos de código fuente
- **config_files**: Archivos de configuración
- **doc_files**: Archivos de documentación

### Métricas Avanzadas (con AdvancedAnalyzer)

- **health_score**: Puntuación de salud (0-100)
- **health_grade**: Calificación (A-F)
- **code_to_config_ratio**: Relación código/configuración
- **recommendations_count**: Número de recomendaciones

## 📈 Score de Salud del Proyecto

El `AdvancedAnalyzer` calcula un score de salud basado en:

| Factor | Impacto | Descripción |
|--------|---------|-------------|
| README presente | -20 | Documentación principal |
| Tests implementados | -15 | Calidad del código |
| CI/CD configurado | -10 | Automatización |
| .gitignore presente | -5 | Control de versiones |
| Dockerizado | -5 | Despliegue |
| Gestión de dependencias | -10 | Mantenibilidad |
| LICENSE presente | -5 | Legal |
| Configuración completa | +5 | Profesionalismo |

**Calificaciones:**
- 90-100: A (Excelente)
- 80-89: B (Bueno)
- 70-79: C (Aceptable)
- 60-69: D (Necesita mejoras)
- 0-59: F (Requiere atención urgente)

## 🐛 Solución de Problemas

### Problema: Análisis muy lento en proyectos grandes

**Solución**: El agente excluye automáticamente directorios pesados. Si sigue lento:

```bash
# Verifica que estos directorios estén excluidos:
# - node_modules
# - .git
# - venv/env
# - __pycache__
# - dist/build/target
```

### Problema: No se detectan tecnologías

**Causa**: Los archivos de configuración deben estar presentes.

**Solución**: Verifica que existan archivos como:
- Python: `requirements.txt`, `setup.py`, `pyproject.toml`
- Node.js: `package.json`
- Java: `pom.xml`, `build.gradle`

### Problema: Errores de permisos

```bash
chmod +x project_resource_agent.py
chmod +x demo_agent.py
chmod +x advanced_usage_example.py
```

### Problema: Reportes muy grandes

**Solución**: El agente limita automáticamente el contenido en reportes Markdown/HTML. Para proyectos grandes, usa JSON y procesa según necesites.

## 🎓 Mejores Prácticas

1. **Ejecuta análisis regularmente**: Semanalmente o por sprint
2. **Versioná los reportes**: Usa timestamps en nombres de archivo
3. **Integra en CI/CD**: Automatiza el análisis en tu pipeline
4. **Comparte con el equipo**: Usa reportes HTML para presentaciones
5. **Actúa sobre recomendaciones**: No ignores las sugerencias
6. **Monitorea tendencias**: Compara análisis en el tiempo
7. **Personaliza para tu contexto**: Adapta reglas a tu organización

## 🔗 Integraciones Disponibles

- ✅ GitHub Actions (plantillas incluidas)
- ✅ GitLab CI (plantillas incluidas)
- ✅ Jenkins (Jenkinsfile incluido)
- ✅ CircleCI (config incluida)
- ✅ Azure Pipelines (plantillas incluidas)
- ✅ Travis CI (config incluida)
- ✅ Bitbucket Pipelines (config incluida)
- ✅ Docker (Dockerfile incluido)
- ✅ Pre-commit hooks
- ✅ Make
- ✅ NPM scripts

Ver `CI_CD_TEMPLATES.md` para todos los ejemplos.

## 📊 Roadmap de Mejoras Futuras

Ideas para extender el agente:

- [ ] Análisis de complejidad ciclomática
- [ ] Detección de código duplicado
- [ ] Análisis de seguridad (vulnerabilidades)
- [ ] Integración con APIs de GitHub/GitLab
- [ ] Generación de diagramas de arquitectura
- [ ] Estimación de esfuerzos de desarrollo
- [ ] Análisis de licencias de dependencias
- [ ] Detección de dead code
- [ ] Métricas de cobertura de tests
- [ ] Dashboard web interactivo
- [ ] Integración con SonarQube
- [ ] Análisis de performance
- [ ] Recomendaciones de refactoring

## 🤝 Contribuir

El código está diseñado para ser extensible:

1. **Añadir tecnologías**: Modifica `TECH_PATTERNS`
2. **Nuevas categorías**: Edita `resource_categories`
3. **Métricas custom**: Extiende `_calculate_metrics()`
4. **Recomendaciones**: Personaliza `_generate_recommendations()`
5. **Formatos de reporte**: Añade métodos `_generate_X_report()`

## 📄 Licencia

Este agente es de código abierto y puede ser usado libremente.

## 📞 Recursos de Ayuda

- **Documentación completa**: `README_AGENT.md`
- **Guía rápida**: `GUIA_RAPIDA.md`
- **Ejemplos avanzados**: `advanced_usage_example.py`
- **Integración CI/CD**: `CI_CD_TEMPLATES.md`
- **Demo interactiva**: `demo_agent.py`

## 🎯 Comandos Rápidos de Referencia

```bash
# Análisis básico
python3 project_resource_agent.py .

# Reporte HTML
python3 project_resource_agent.py . -f html -o reporte.html

# Reporte JSON
python3 project_resource_agent.py . -f json -o datos.json

# Reporte Markdown
python3 project_resource_agent.py . -f markdown -o ANALISIS.md

# Demo completa
python3 demo_agent.py

# Ejemplos avanzados
python3 advanced_usage_example.py

# Ver ayuda
python3 project_resource_agent.py --help
```

## 🌟 Características Destacadas

✨ **Sin dependencias externas** - Solo Python estándar
🚀 **Rápido y eficiente** - Analiza miles de archivos en segundos
📊 **Múltiples formatos** - Markdown, JSON, HTML
🔍 **Detección inteligente** - Reconoce 12+ tecnologías
💡 **Recomendaciones prácticas** - Basadas en mejores prácticas
🛠️ **Altamente personalizable** - Código modular y extensible
🐳 **Listo para Docker** - Dockerfiles incluidos
🔗 **Integración CI/CD** - Plantillas para todas las plataformas
📚 **Documentación completa** - Guías y ejemplos incluidos
🎓 **Fácil de usar** - CLI intuitiva con ayuda integrada

---

## 🚀 ¡Empieza Ahora!

```bash
# 1. Ejecuta la demo
python3 demo_agent.py

# 2. Analiza tu proyecto
python3 project_resource_agent.py /tu/proyecto

# 3. Explora las capacidades avanzadas
python3 advanced_usage_example.py

# 4. Integra en tu CI/CD
# Ver CI_CD_TEMPLATES.md
```

**¡Listo para analizar proyectos de cualquier tamaño y complejidad!** 🎉
