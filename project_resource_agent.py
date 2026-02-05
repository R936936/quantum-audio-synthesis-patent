#!/usr/bin/env python3
"""
Agente Híbrido Especialista en Análisis y Levantamiento de Recursos para Proyectos
==================================================================================

Este agente combina múltiples capacidades para:
- Analizar estructura de proyectos
- Identificar recursos (código, archivos, dependencias)
- Generar documentación técnica
- Estimar esfuerzos y requisitos
- Proporcionar recomendaciones
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import re
import subprocess


@dataclass
class Resource:
    """Representa un recurso del proyecto"""
    name: str
    type: str
    path: str
    size: Optional[int] = None
    description: str = ""
    dependencies: List[str] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []


@dataclass
class ProjectAnalysis:
    """Resultado del análisis del proyecto"""
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


class ProjectResourceAgent:
    """Agente principal para análisis y levantamiento de recursos"""
    
    TECH_PATTERNS = {
        'python': ['.py', 'requirements.txt', 'setup.py', 'pyproject.toml', 'Pipfile'],
        'javascript': ['.js', '.jsx', 'package.json', 'package-lock.json'],
        'typescript': ['.ts', '.tsx', 'tsconfig.json'],
        'java': ['.java', 'pom.xml', 'build.gradle', 'gradle.properties'],
        'go': ['.go', 'go.mod', 'go.sum'],
        'rust': ['.rs', 'Cargo.toml', 'Cargo.lock'],
        'php': ['.php', 'composer.json', 'composer.lock'],
        'ruby': ['.rb', 'Gemfile', 'Gemfile.lock'],
        'csharp': ['.cs', '.csproj', '.sln'],
        'docker': ['Dockerfile', 'docker-compose.yml', '.dockerignore'],
        'kubernetes': ['.yaml', '.yml', 'k8s'],
        'terraform': ['.tf', 'terraform.tfstate'],
        'ansible': ['playbook.yml', 'ansible.cfg'],
    }
    
    CONFIG_FILES = [
        '.env', '.env.example', 'config.json', 'config.yaml', 'settings.py',
        '.gitignore', '.dockerignore', 'Makefile', 'README.md', 'LICENSE'
    ]
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self.project_name = self.project_path.name
        self.resources: List[Resource] = []
        self.technologies: set = set()
        self.dependencies: Dict[str, List[str]] = {}
        self.file_count = 0
        self.total_size = 0
        
    def analyze(self) -> ProjectAnalysis:
        """Ejecuta el análisis completo del proyecto"""
        print(f"🔍 Analizando proyecto: {self.project_name}")
        print(f"📁 Ruta: {self.project_path}\n")
        
        # Verificar que el directorio existe
        if not self.project_path.exists():
            raise ValueError(f"El directorio {self.project_path} no existe")
        
        # Fases del análisis
        self._scan_files()
        self._detect_technologies()
        self._analyze_dependencies()
        self._identify_resources()
        metrics = self._calculate_metrics()
        recommendations = self._generate_recommendations()
        
        # Crear resultado del análisis
        analysis = ProjectAnalysis(
            project_name=self.project_name,
            root_path=str(self.project_path),
            timestamp=datetime.now().isoformat(),
            resources=self.resources,
            technologies=sorted(list(self.technologies)),
            dependencies=self.dependencies,
            file_count=self.file_count,
            total_size=self.total_size,
            recommendations=recommendations,
            metrics=metrics
        )
        
        return analysis
    
    def _scan_files(self):
        """Escanea todos los archivos del proyecto"""
        print("📊 Fase 1: Escaneando archivos...")
        
        exclude_dirs = {
            '.git', '__pycache__', 'node_modules', 'venv', 'env',
            '.venv', 'dist', 'build', 'target', '.idea', '.vscode',
            'vendor', 'bin', 'obj', '.pytest_cache', 'coverage'
        }
        
        for root, dirs, files in os.walk(self.project_path):
            # Excluir directorios no deseados
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                file_path = Path(root) / file
                try:
                    file_size = file_path.stat().st_size
                    self.file_count += 1
                    self.total_size += file_size
                except (OSError, PermissionError):
                    continue
        
        print(f"   ✓ {self.file_count} archivos encontrados ({self._format_size(self.total_size)})\n")
    
    def _detect_technologies(self):
        """Detecta las tecnologías utilizadas en el proyecto"""
        print("🔧 Fase 2: Detectando tecnologías...")
        
        for root, dirs, files in os.walk(self.project_path):
            # Excluir directorios
            dirs[:] = [d for d in dirs if d not in {'.git', 'node_modules', 'venv'}]
            
            for file in files:
                file_lower = file.lower()
                
                for tech, patterns in self.TECH_PATTERNS.items():
                    for pattern in patterns:
                        if file_lower.endswith(pattern) or file_lower == pattern:
                            self.technologies.add(tech)
        
        if self.technologies:
            print(f"   ✓ Tecnologías detectadas: {', '.join(sorted(self.technologies))}\n")
        else:
            print("   ⚠ No se detectaron tecnologías específicas\n")
    
    def _analyze_dependencies(self):
        """Analiza las dependencias del proyecto"""
        print("📦 Fase 3: Analizando dependencias...")
        
        # Python dependencies
        self._parse_python_dependencies()
        
        # JavaScript/Node dependencies
        self._parse_nodejs_dependencies()
        
        # Java dependencies
        self._parse_java_dependencies()
        
        # Go dependencies
        self._parse_go_dependencies()
        
        total_deps = sum(len(deps) for deps in self.dependencies.values())
        print(f"   ✓ {total_deps} dependencias encontradas\n")
    
    def _parse_python_dependencies(self):
        """Parsea dependencias de Python"""
        requirements_files = [
            'requirements.txt', 'requirements-dev.txt', 
            'requirements-test.txt', 'dev-requirements.txt'
        ]
        
        for req_file in requirements_files:
            req_path = self.project_path / req_file
            if req_path.exists():
                try:
                    with open(req_path, 'r', encoding='utf-8') as f:
                        deps = []
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith('#'):
                                # Extraer nombre del paquete
                                pkg = re.split(r'[=<>!]', line)[0].strip()
                                if pkg:
                                    deps.append(line)
                        if deps:
                            self.dependencies[req_file] = deps
                except Exception as e:
                    print(f"   ⚠ Error leyendo {req_file}: {e}")
        
        # pyproject.toml
        pyproject = self.project_path / 'pyproject.toml'
        if pyproject.exists():
            try:
                with open(pyproject, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Extraer dependencias básicas
                    if '[tool.poetry.dependencies]' in content:
                        self.dependencies['pyproject.toml (poetry)'] = ['Ver archivo para detalles']
            except Exception:
                pass
    
    def _parse_nodejs_dependencies(self):
        """Parsea dependencias de Node.js"""
        package_json = self.project_path / 'package.json'
        if package_json.exists():
            try:
                with open(package_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    if 'dependencies' in data:
                        self.dependencies['npm dependencies'] = [
                            f"{k}@{v}" for k, v in data['dependencies'].items()
                        ]
                    
                    if 'devDependencies' in data:
                        self.dependencies['npm devDependencies'] = [
                            f"{k}@{v}" for k, v in data['devDependencies'].items()
                        ]
            except Exception as e:
                print(f"   ⚠ Error leyendo package.json: {e}")
    
    def _parse_java_dependencies(self):
        """Parsea dependencias de Java"""
        pom_xml = self.project_path / 'pom.xml'
        if pom_xml.exists():
            self.dependencies['maven (pom.xml)'] = ['Ver pom.xml para detalles completos']
        
        build_gradle = self.project_path / 'build.gradle'
        if build_gradle.exists():
            self.dependencies['gradle (build.gradle)'] = ['Ver build.gradle para detalles completos']
    
    def _parse_go_dependencies(self):
        """Parsea dependencias de Go"""
        go_mod = self.project_path / 'go.mod'
        if go_mod.exists():
            try:
                with open(go_mod, 'r', encoding='utf-8') as f:
                    deps = []
                    for line in f:
                        line = line.strip()
                        if line.startswith('require'):
                            continue
                        if line and not line.startswith('//') and not line.startswith('module'):
                            deps.append(line)
                    if deps:
                        self.dependencies['go.mod'] = deps
            except Exception:
                pass
    
    def _identify_resources(self):
        """Identifica y categoriza los recursos del proyecto"""
        print("🎯 Fase 4: Identificando recursos clave...")
        
        resource_categories = {
            'source_code': ['.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.go', '.rs', '.php', '.rb', '.cs'],
            'configuration': self.CONFIG_FILES,
            'documentation': ['README.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'LICENSE', 'docs/'],
            'tests': ['test_', '_test.', 'spec.', '.test.', '.spec.'],
            'database': ['.sql', '.sqlite', '.db', 'migrations/'],
            'static': ['.css', '.scss', '.sass', '.less', '.html', '.htm'],
            'media': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.mp4', '.mp3'],
            'data': ['.json', '.yaml', '.yml', '.xml', '.csv', '.toml'],
        }
        
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in {'.git', 'node_modules', 'venv', '__pycache__'}]
            
            for file in files:
                file_path = Path(root) / file
                rel_path = file_path.relative_to(self.project_path)
                
                # Determinar categoría
                category = 'other'
                for cat, patterns in resource_categories.items():
                    for pattern in patterns:
                        if file.endswith(pattern) or pattern in str(rel_path) or file.startswith(pattern):
                            category = cat
                            break
                    if category != 'other':
                        break
                
                # Crear recurso solo para archivos relevantes
                if category in ['source_code', 'configuration', 'documentation', 'database']:
                    try:
                        size = file_path.stat().st_size
                        resource = Resource(
                            name=file,
                            type=category,
                            path=str(rel_path),
                            size=size,
                            description=self._get_file_description(file, category)
                        )
                        self.resources.append(resource)
                    except (OSError, PermissionError):
                        continue
        
        print(f"   ✓ {len(self.resources)} recursos clave identificados\n")
    
    def _get_file_description(self, filename: str, category: str) -> str:
        """Genera una descripción para un archivo"""
        descriptions = {
            'requirements.txt': 'Dependencias Python del proyecto',
            'package.json': 'Configuración y dependencias Node.js',
            'Dockerfile': 'Configuración de contenedor Docker',
            'docker-compose.yml': 'Orquestación de servicios Docker',
            'README.md': 'Documentación principal del proyecto',
            '.env': 'Variables de entorno',
            '.gitignore': 'Archivos ignorados por Git',
            'Makefile': 'Automatización de tareas',
            'setup.py': 'Configuración de instalación Python',
            'go.mod': 'Módulo y dependencias Go',
            'pom.xml': 'Configuración Maven',
            'build.gradle': 'Configuración Gradle',
        }
        
        return descriptions.get(filename, f"Archivo de tipo {category}")
    
    def _calculate_metrics(self) -> Dict[str, Any]:
        """Calcula métricas del proyecto"""
        print("📈 Fase 5: Calculando métricas...")
        
        metrics = {
            'total_files': self.file_count,
            'total_size_bytes': self.total_size,
            'total_size_human': self._format_size(self.total_size),
            'technologies_count': len(self.technologies),
            'dependency_groups': len(self.dependencies),
            'resource_categories': {},
            'code_files': 0,
            'config_files': 0,
            'doc_files': 0,
        }
        
        # Contar recursos por categoría
        for resource in self.resources:
            metrics['resource_categories'][resource.type] = \
                metrics['resource_categories'].get(resource.type, 0) + 1
            
            if resource.type == 'source_code':
                metrics['code_files'] += 1
            elif resource.type == 'configuration':
                metrics['config_files'] += 1
            elif resource.type == 'documentation':
                metrics['doc_files'] += 1
        
        print("   ✓ Métricas calculadas\n")
        return metrics
    
    def _generate_recommendations(self) -> List[str]:
        """Genera recomendaciones basadas en el análisis"""
        print("💡 Fase 6: Generando recomendaciones...")
        
        recommendations = []
        
        # Verificar README
        readme_exists = any(r.name.upper() == 'README.MD' for r in self.resources)
        if not readme_exists:
            recommendations.append("📝 Se recomienda agregar un archivo README.md con documentación del proyecto")
        
        # Verificar archivo de dependencias
        has_deps_file = any(k in str(self.dependencies.keys()) for k in ['requirements.txt', 'package.json', 'go.mod'])
        if not has_deps_file and self.technologies:
            recommendations.append("📦 Considerar agregar un archivo de gestión de dependencias")
        
        # Verificar .gitignore
        gitignore_exists = any(r.name == '.gitignore' for r in self.resources)
        if not gitignore_exists:
            recommendations.append("🔒 Se recomienda agregar un archivo .gitignore")
        
        # Verificar LICENSE
        license_exists = any('LICENSE' in r.name.upper() for r in self.resources)
        if not license_exists:
            recommendations.append("⚖️ Considerar agregar un archivo LICENSE al proyecto")
        
        # Verificar tests
        test_files = [r for r in self.resources if 'test' in r.path.lower()]
        if not test_files:
            recommendations.append("🧪 Se recomienda implementar tests automatizados")
        
        # Verificar CI/CD
        ci_files = ['.github/workflows', '.gitlab-ci.yml', 'Jenkinsfile', '.circleci']
        has_ci = any(any(ci in r.path for ci in ci_files) for r in self.resources)
        if not has_ci:
            recommendations.append("🚀 Considerar implementar CI/CD (GitHub Actions, GitLab CI, etc.)")
        
        # Docker
        has_docker = 'docker' in self.technologies
        if not has_docker and len(self.technologies) > 0:
            recommendations.append("🐳 Considerar dockerizar la aplicación para facilitar el despliegue")
        
        # Documentación de API
        if 'python' in self.technologies or 'javascript' in self.technologies:
            recommendations.append("📚 Considerar documentar APIs con Swagger/OpenAPI")
        
        # Tamaño del proyecto
        if self.total_size > 100 * 1024 * 1024:  # 100 MB
            recommendations.append("💾 El proyecto es grande, considerar optimizar recursos o usar Git LFS")
        
        print(f"   ✓ {len(recommendations)} recomendaciones generadas\n")
        return recommendations
    
    def _format_size(self, size: int) -> str:
        """Formatea el tamaño en bytes a formato legible"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"
    
    def generate_report(self, analysis: ProjectAnalysis, output_format: str = 'markdown') -> str:
        """Genera un reporte del análisis"""
        if output_format == 'markdown':
            return self._generate_markdown_report(analysis)
        elif output_format == 'json':
            return self._generate_json_report(analysis)
        elif output_format == 'html':
            return self._generate_html_report(analysis)
        else:
            raise ValueError(f"Formato no soportado: {output_format}")
    
    def _generate_markdown_report(self, analysis: ProjectAnalysis) -> str:
        """Genera un reporte en formato Markdown"""
        report = f"""# 📊 Análisis de Recursos del Proyecto: {analysis.project_name}

**Fecha de análisis:** {analysis.timestamp}
**Ruta del proyecto:** `{analysis.root_path}`

---

## 📈 Resumen Ejecutivo

- **Total de archivos:** {analysis.file_count:,}
- **Tamaño total:** {analysis.metrics['total_size_human']}
- **Tecnologías detectadas:** {len(analysis.technologies)}
- **Grupos de dependencias:** {len(analysis.dependencies)}
- **Recursos clave identificados:** {len(analysis.resources)}

---

## 🔧 Tecnologías Detectadas

"""
        if analysis.technologies:
            for tech in analysis.technologies:
                report += f"- **{tech.capitalize()}**\n"
        else:
            report += "*No se detectaron tecnologías específicas*\n"
        
        report += "\n---\n\n## 📦 Dependencias\n\n"
        
        if analysis.dependencies:
            for dep_file, deps in analysis.dependencies.items():
                report += f"### {dep_file}\n\n"
                if len(deps) > 10:
                    report += f"*{len(deps)} dependencias encontradas*\n\n"
                    for dep in deps[:5]:
                        report += f"- {dep}\n"
                    report += f"- ... y {len(deps) - 5} más\n\n"
                else:
                    for dep in deps:
                        report += f"- {dep}\n"
                    report += "\n"
        else:
            report += "*No se encontraron archivos de dependencias*\n\n"
        
        report += "---\n\n## 🎯 Recursos Clave del Proyecto\n\n"
        
        # Agrupar recursos por categoría
        resources_by_category = {}
        for resource in analysis.resources:
            if resource.type not in resources_by_category:
                resources_by_category[resource.type] = []
            resources_by_category[resource.type].append(resource)
        
        for category, resources in sorted(resources_by_category.items()):
            report += f"### {category.replace('_', ' ').title()} ({len(resources)} archivos)\n\n"
            report += "| Archivo | Ruta | Tamaño | Descripción |\n"
            report += "|---------|------|--------|-------------|\n"
            
            # Mostrar máximo 15 recursos por categoría
            for resource in resources[:15]:
                size_str = self._format_size(resource.size) if resource.size else 'N/A'
                report += f"| {resource.name} | `{resource.path}` | {size_str} | {resource.description} |\n"
            
            if len(resources) > 15:
                report += f"\n*... y {len(resources) - 15} archivos más*\n"
            
            report += "\n"
        
        report += "---\n\n## 💡 Recomendaciones\n\n"
        
        if analysis.recommendations:
            for i, rec in enumerate(analysis.recommendations, 1):
                report += f"{i}. {rec}\n"
        else:
            report += "*No hay recomendaciones adicionales*\n"
        
        report += "\n---\n\n## 📊 Métricas Detalladas\n\n"
        report += "```json\n"
        report += json.dumps(analysis.metrics, indent=2, ensure_ascii=False)
        report += "\n```\n\n"
        
        report += "---\n\n"
        report += "*Reporte generado por el Agente Híbrido de Análisis de Recursos*\n"
        
        return report
    
    def _generate_json_report(self, analysis: ProjectAnalysis) -> str:
        """Genera un reporte en formato JSON"""
        data = {
            'project_name': analysis.project_name,
            'root_path': analysis.root_path,
            'timestamp': analysis.timestamp,
            'summary': {
                'file_count': analysis.file_count,
                'total_size': analysis.total_size,
                'technologies': analysis.technologies,
            },
            'technologies': analysis.technologies,
            'dependencies': analysis.dependencies,
            'resources': [asdict(r) for r in analysis.resources],
            'metrics': analysis.metrics,
            'recommendations': analysis.recommendations,
        }
        
        return json.dumps(data, indent=2, ensure_ascii=False)
    
    def _generate_html_report(self, analysis: ProjectAnalysis) -> str:
        """Genera un reporte en formato HTML"""
        html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Análisis de {analysis.project_name}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        .metric {{
            display: inline-block;
            background: #ecf0f1;
            padding: 15px 25px;
            margin: 10px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }}
        .metric strong {{ display: block; font-size: 24px; color: #2c3e50; }}
        .tech-badge {{
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 5px 15px;
            margin: 5px;
            border-radius: 20px;
            font-size: 14px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background: #34495e;
            color: white;
        }}
        tr:hover {{ background: #f5f5f5; }}
        .recommendation {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 10px 15px;
            margin: 10px 0;
        }}
        .category {{ margin: 20px 0; }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Análisis de Recursos: {analysis.project_name}</h1>
        <p><strong>Fecha:</strong> {analysis.timestamp}</p>
        <p><strong>Ruta:</strong> <code>{analysis.root_path}</code></p>
        
        <h2>📈 Resumen Ejecutivo</h2>
        <div class="metrics">
            <div class="metric">
                <strong>{analysis.file_count:,}</strong>
                <span>Archivos</span>
            </div>
            <div class="metric">
                <strong>{analysis.metrics['total_size_human']}</strong>
                <span>Tamaño Total</span>
            </div>
            <div class="metric">
                <strong>{len(analysis.technologies)}</strong>
                <span>Tecnologías</span>
            </div>
            <div class="metric">
                <strong>{len(analysis.resources)}</strong>
                <span>Recursos Clave</span>
            </div>
        </div>
        
        <h2>🔧 Tecnologías Detectadas</h2>
        <div>
"""
        
        for tech in analysis.technologies:
            html += f'            <span class="tech-badge">{tech.capitalize()}</span>\n'
        
        html += """        </div>
        
        <h2>💡 Recomendaciones</h2>
"""
        
        for rec in analysis.recommendations:
            html += f'        <div class="recommendation">{rec}</div>\n'
        
        html += """        
        <h2>📦 Dependencias</h2>
"""
        
        for dep_file, deps in analysis.dependencies.items():
            html += f'        <h3>{dep_file}</h3>\n'
            html += f'        <p><em>{len(deps)} dependencias encontradas</em></p>\n'
        
        html += """    </div>
</body>
</html>"""
        
        return html


def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Agente Híbrido de Análisis y Levantamiento de Recursos para Proyectos',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  %(prog)s /ruta/al/proyecto
  %(prog)s . --format json --output reporte.json
  %(prog)s ~/mi-proyecto --format html --output reporte.html
        """
    )
    
    parser.add_argument(
        'project_path',
        nargs='?',
        default='.',
        help='Ruta al proyecto a analizar (por defecto: directorio actual)'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['markdown', 'json', 'html'],
        default='markdown',
        help='Formato del reporte (por defecto: markdown)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Archivo de salida para el reporte (por defecto: stdout)'
    )
    
    parser.add_argument(
        '--no-color',
        action='store_true',
        help='Desactivar colores en la salida'
    )
    
    args = parser.parse_args()
    
    try:
        # Crear agente y analizar proyecto
        agent = ProjectResourceAgent(args.project_path)
        analysis = agent.analyze()
        
        # Generar reporte
        print("=" * 70)
        print("📝 Generando reporte...\n")
        report = agent.generate_report(analysis, args.format)
        
        # Guardar o mostrar reporte
        if args.output:
            output_path = Path(args.output)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"✅ Reporte guardado en: {output_path.resolve()}")
        else:
            print("\n" + "=" * 70)
            print(report)
        
        print("\n" + "=" * 70)
        print("✨ Análisis completado exitosamente!")
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
