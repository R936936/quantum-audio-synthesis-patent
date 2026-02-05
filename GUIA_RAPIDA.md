# 🚀 Guía Rápida - Agente Híbrido de Análisis de Recursos

## ⚡ Inicio Rápido (2 minutos)

### 1. Ejecutar Demostración

```bash
# Ejecutar la demostración completa
python3 demo_agent.py
```

Esto creará un proyecto de ejemplo y mostrará todas las capacidades del agente.

### 2. Analizar Tu Proyecto

```bash
# Analizar el directorio actual
python3 project_resource_agent.py

# Analizar un proyecto específico
python3 project_resource_agent.py /ruta/a/tu/proyecto
```

### 3. Generar Reportes

```bash
# Reporte en consola (Markdown)
python3 project_resource_agent.py . > ANALISIS.md

# Reporte JSON para procesamiento automático
python3 project_resource_agent.py . --format json --output analisis.json

# Reporte HTML para visualización en navegador
python3 project_resource_agent.py . --format html --output reporte.html
```

## 📋 Comandos Más Usados

### Análisis Básico

```bash
# Proyecto actual
python3 project_resource_agent.py

# Proyecto específico
python3 project_resource_agent.py ~/mi-proyecto
```

### Exportar Reportes

```bash
# Markdown (documentación)
python3 project_resource_agent.py . -f markdown -o ESTRUCTURA.md

# JSON (integración con herramientas)
python3 project_resource_agent.py . -f json -o datos.json

# HTML (presentación)
python3 project_resource_agent.py . -f html -o informe.html
```

### Ver Ayuda

```bash
python3 project_resource_agent.py --help
```

## 🎯 Casos de Uso Comunes

### 1. Auditoría Rápida

```bash
# Generar reporte HTML para revisión
python3 project_resource_agent.py /proyecto-legacy --format html -o auditoria.html

# Abrir en navegador
open auditoria.html  # macOS
xdg-open auditoria.html  # Linux
start auditoria.html  # Windows
```

### 2. Documentación de Estructura

```bash
# Generar documentación Markdown
python3 project_resource_agent.py . -f markdown -o ESTRUCTURA.md

# Agregar al README o wiki del proyecto
cat ESTRUCTURA.md >> README.md
```

### 3. Análisis de Dependencias

```bash
# Exportar dependencias en JSON
python3 project_resource_agent.py . -f json -o deps.json

# Procesar con jq (si está instalado)
python3 project_resource_agent.py . -f json | jq '.dependencies'
```

### 4. Integración en CI/CD

```bash
# En tu pipeline (GitHub Actions, GitLab CI, etc.)
python3 project_resource_agent.py . -f json -o build/analisis.json

# Usar el reporte para decisiones automáticas
if [ $(jq '.file_count' build/analisis.json) -gt 10000 ]; then
  echo "Proyecto muy grande, considerar optimización"
fi
```

### 5. Onboarding de Desarrolladores

```bash
# Generar reporte completo para nuevos miembros
python3 project_resource_agent.py . -f html -o docs/onboarding.html

# Compartir vía email o wiki
```

## 💡 Tips y Trucos

### 1. Análisis Rápido de Múltiples Proyectos

```bash
#!/bin/bash
for dir in ~/proyectos/*; do
  if [ -d "$dir" ]; then
    echo "Analizando: $dir"
    python3 project_resource_agent.py "$dir" -f json -o "analisis_$(basename $dir).json"
  fi
done
```

### 2. Comparar Dos Versiones de un Proyecto

```bash
# Versión actual
python3 project_resource_agent.py . -f json -o analisis_actual.json

# Después de cambios...
python3 project_resource_agent.py . -f json -o analisis_nuevo.json

# Comparar con diff o herramientas JSON
diff analisis_actual.json analisis_nuevo.json
```

### 3. Integrar con Git Hooks

```bash
# .git/hooks/pre-commit
#!/bin/bash
python3 project_resource_agent.py . -f json -o .project_analysis.json
git add .project_analysis.json
```

### 4. Uso Programático en Python

```python
from project_resource_agent import ProjectResourceAgent

# Analizar proyecto
agent = ProjectResourceAgent('.')
analysis = agent.analyze()

# Obtener métricas específicas
print(f"Tecnologías: {analysis.technologies}")
print(f"Archivos: {analysis.file_count}")

# Filtrar recursos
code_files = [r for r in analysis.resources if r.type == 'source_code']
print(f"Archivos de código: {len(code_files)}")

# Generar reporte personalizado
report = agent.generate_report(analysis, 'json')
```

### 5. Automatizar con Cron

```bash
# Añadir a crontab (análisis semanal)
0 9 * * 1 cd /proyecto && python3 /ruta/project_resource_agent.py . -f html -o /reports/weekly_$(date +\%Y\%m\%d).html
```

## 🔧 Personalización

### Modificar Exclusiones

Edita en `project_resource_agent.py`:

```python
exclude_dirs = {
    '.git', '__pycache__', 'node_modules', 'venv',
    # Añade tus directorios
    'mis_exclusiones', 'temp'
}
```

### Agregar Nuevas Tecnologías

```python
TECH_PATTERNS = {
    'mi_lenguaje': ['.ext', 'config.file'],
    # ...
}
```

## 📊 Interpretar Resultados

### Métricas Clave

- **file_count**: Número total de archivos (excluye directorios comunes)
- **total_size**: Tamaño del proyecto (útil para planificación)
- **technologies**: Lenguajes/frameworks detectados
- **resource_categories**: Distribución de tipos de archivos

### Recomendaciones

Las recomendaciones son sugerencias basadas en:
- Presencia/ausencia de archivos importantes
- Mejores prácticas de la industria
- Tamaño y complejidad del proyecto

## 🐛 Solución Rápida de Problemas

### Problema: "No such file or directory"
**Solución**: Verifica la ruta del proyecto
```bash
python3 project_resource_agent.py $(pwd)
```

### Problema: "Permission denied"
**Solución**: Verifica permisos
```bash
chmod +x project_resource_agent.py
```

### Problema: Análisis muy lento
**Solución**: Excluye directorios grandes
- El agente ya excluye `node_modules`, `venv`, etc.
- Verifica que `.gitignore` esté configurado

### Problema: No se detectan tecnologías
**Solución**: Verifica nombres de archivos
- Deben estar en el directorio raíz o subdirectorios
- Ejemplo: `requirements.txt`, `package.json`

## 📚 Recursos Adicionales

- **Documentación completa**: Ver `README_AGENT.md`
- **Código fuente**: `project_resource_agent.py`
- **Demostración**: `demo_agent.py`

## 🎓 Ejemplos Avanzados

### Script de Análisis Comparativo

```python
#!/usr/bin/env python3
from project_resource_agent import ProjectResourceAgent
import json

projects = ['/proyecto1', '/proyecto2', '/proyecto3']
results = {}

for project in projects:
    agent = ProjectResourceAgent(project)
    analysis = agent.analyze()
    results[project] = {
        'files': analysis.file_count,
        'size': analysis.total_size,
        'technologies': analysis.technologies,
        'recommendations': len(analysis.recommendations)
    }

# Imprimir comparación
print(json.dumps(results, indent=2))
```

### Generar Dashboard

```python
#!/usr/bin/env python3
from project_resource_agent import ProjectResourceAgent
import json

# Analizar múltiples proyectos
projects = {
    'API Backend': '/path/to/api',
    'Frontend': '/path/to/frontend',
    'Mobile App': '/path/to/mobile'
}

dashboard_data = []
for name, path in projects.items():
    agent = ProjectResourceAgent(path)
    analysis = agent.analyze()
    dashboard_data.append({
        'name': name,
        'metrics': analysis.metrics,
        'health_score': calculate_health_score(analysis)
    })

# Guardar para visualización
with open('dashboard.json', 'w') as f:
    json.dump(dashboard_data, f, indent=2)
```

## ⭐ Mejores Prácticas

1. **Ejecuta análisis regularmente**: Idealmente cada sprint o release
2. **Versioná los reportes**: Permite tracking de evolución
3. **Revisa recomendaciones**: No todas aplican a todos los proyectos
4. **Combina con otras herramientas**: SonarQube, ESLint, etc.
5. **Comparte con el equipo**: Usa reportes HTML para reuniones

## 🔗 Workflows Sugeridos

### Para Equipos Ágiles

```bash
# Sprint Planning
python3 project_resource_agent.py . -f html -o sprint_inicio.html

# Sprint Review
python3 project_resource_agent.py . -f html -o sprint_fin.html

# Comparar
diff sprint_inicio.html sprint_fin.html
```

### Para DevOps

```bash
# Pre-deployment check
python3 project_resource_agent.py . -f json | \
  jq '.recommendations' > pre_deploy_check.txt
```

### Para Arquitectos

```bash
# Análisis de arquitectura
python3 project_resource_agent.py . -f json | \
  jq '{tech: .technologies, deps: .dependencies, metrics: .metrics}' \
  > architecture_review.json
```

---

**¿Necesitas más ayuda?** Consulta `README_AGENT.md` para documentación completa.

**¿Encontraste un bug?** Revisa el código en `project_resource_agent.py`.

**¿Quieres contribuir?** El código está diseñado para ser extensible.
