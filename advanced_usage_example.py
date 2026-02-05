#!/usr/bin/env python3
"""
Ejemplos Avanzados de Uso del Agente Híbrido de Análisis de Recursos

Este script demuestra casos de uso avanzados:
- Análisis comparativo de múltiples proyectos
- Cálculo de métricas de salud del proyecto
- Generación de reportes consolidados
- Integración con sistemas de métricas
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from project_resource_agent import ProjectResourceAgent, ProjectAnalysis


class AdvancedAnalyzer:
    """Analizador avanzado con capacidades extendidas"""
    
    def __init__(self):
        self.analyses: List[ProjectAnalysis] = []
    
    def analyze_projects(self, project_paths: List[str]) -> List[ProjectAnalysis]:
        """Analiza múltiples proyectos"""
        print("🔍 Analizando múltiples proyectos...\n")
        
        for path in project_paths:
            try:
                print(f"📁 Procesando: {path}")
                agent = ProjectResourceAgent(path)
                analysis = agent.analyze()
                self.analyses.append(analysis)
                print(f"   ✓ Completado\n")
            except Exception as e:
                print(f"   ❌ Error: {e}\n")
        
        return self.analyses
    
    def calculate_health_score(self, analysis: ProjectAnalysis) -> Dict[str, Any]:
        """Calcula un score de salud del proyecto (0-100)"""
        score = 100
        factors = {}
        
        # Factor 1: Documentación (-20 si no hay README)
        has_readme = any('README' in r.name.upper() for r in analysis.resources)
        if not has_readme:
            score -= 20
            factors['documentation'] = 'Missing README (-20)'
        else:
            factors['documentation'] = 'Has README (0)'
        
        # Factor 2: Tests (-15 si no hay tests)
        has_tests = any('test' in r.path.lower() for r in analysis.resources)
        if not has_tests:
            score -= 15
            factors['testing'] = 'No tests found (-15)'
        else:
            factors['testing'] = 'Has tests (0)'
        
        # Factor 3: CI/CD (-10 si no hay configuración)
        ci_patterns = ['.github/workflows', '.gitlab-ci', 'Jenkinsfile', '.circleci']
        has_ci = any(any(ci in r.path for ci in ci_patterns) for r in analysis.resources)
        if not has_ci:
            score -= 10
            factors['ci_cd'] = 'No CI/CD configuration (-10)'
        else:
            factors['ci_cd'] = 'Has CI/CD (0)'
        
        # Factor 4: .gitignore (-5 si no existe)
        has_gitignore = any(r.name == '.gitignore' for r in analysis.resources)
        if not has_gitignore:
            score -= 5
            factors['version_control'] = 'No .gitignore (-5)'
        else:
            factors['version_control'] = 'Has .gitignore (0)'
        
        # Factor 5: Docker (-5 si no hay pero sería útil)
        has_docker = 'docker' in analysis.technologies
        if not has_docker and len(analysis.technologies) > 0:
            score -= 5
            factors['containerization'] = 'Not dockerized (-5)'
        else:
            factors['containerization'] = 'Dockerized or N/A (0)'
        
        # Factor 6: Dependencias gestionadas (+10 si existe)
        has_deps = len(analysis.dependencies) > 0
        if has_deps:
            factors['dependencies'] = 'Dependencies managed (0)'
        else:
            score -= 10
            factors['dependencies'] = 'No dependency management (-10)'
        
        # Factor 7: Licencia (-5 si no existe)
        has_license = any('LICENSE' in r.name.upper() for r in analysis.resources)
        if not has_license:
            score -= 5
            factors['license'] = 'No LICENSE file (-5)'
        else:
            factors['license'] = 'Has LICENSE (0)'
        
        # Bonus: Configuración completa
        config_files = [r for r in analysis.resources if r.type == 'configuration']
        if len(config_files) >= 5:
            score += 5
            factors['configuration'] = 'Well configured (+5)'
        
        # Asegurar que el score esté entre 0-100
        score = max(0, min(100, score))
        
        return {
            'score': score,
            'grade': self._get_grade(score),
            'factors': factors,
            'recommendations_count': len(analysis.recommendations)
        }
    
    def _get_grade(self, score: int) -> str:
        """Convierte el score en una calificación"""
        if score >= 90:
            return 'A (Excelente)'
        elif score >= 80:
            return 'B (Bueno)'
        elif score >= 70:
            return 'C (Aceptable)'
        elif score >= 60:
            return 'D (Necesita mejoras)'
        else:
            return 'F (Requiere atención urgente)'
    
    def generate_comparison_report(self) -> Dict[str, Any]:
        """Genera un reporte comparativo de todos los proyectos analizados"""
        if not self.analyses:
            return {}
        
        comparison = {
            'total_projects': len(self.analyses),
            'timestamp': self.analyses[0].timestamp if self.analyses else '',
            'projects': []
        }
        
        for analysis in self.analyses:
            health = self.calculate_health_score(analysis)
            
            project_data = {
                'name': analysis.project_name,
                'path': analysis.root_path,
                'metrics': {
                    'files': analysis.file_count,
                    'size': analysis.metrics['total_size_human'],
                    'size_bytes': analysis.total_size,
                    'technologies': analysis.technologies,
                    'dependencies_groups': len(analysis.dependencies),
                    'code_files': analysis.metrics.get('code_files', 0),
                    'config_files': analysis.metrics.get('config_files', 0),
                    'doc_files': analysis.metrics.get('doc_files', 0),
                },
                'health': health,
                'recommendations_count': len(analysis.recommendations),
                'top_recommendations': analysis.recommendations[:3]
            }
            
            comparison['projects'].append(project_data)
        
        # Agregar estadísticas globales
        total_files = sum(p['metrics']['files'] for p in comparison['projects'])
        total_size = sum(p['metrics']['size_bytes'] for p in comparison['projects'])
        avg_health = sum(p['health']['score'] for p in comparison['projects']) / len(comparison['projects'])
        
        comparison['summary'] = {
            'total_files': total_files,
            'total_size_bytes': total_size,
            'total_size_human': self._format_size(total_size),
            'average_health_score': round(avg_health, 2),
            'average_health_grade': self._get_grade(int(avg_health)),
            'best_project': max(comparison['projects'], key=lambda x: x['health']['score'])['name'],
            'needs_attention': [p['name'] for p in comparison['projects'] if p['health']['score'] < 70]
        }
        
        return comparison
    
    def _format_size(self, size: int) -> str:
        """Formatea el tamaño en bytes a formato legible"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"
    
    def generate_markdown_comparison(self, comparison: Dict[str, Any]) -> str:
        """Genera un reporte comparativo en Markdown"""
        md = f"""# 📊 Reporte Comparativo de Proyectos

**Total de proyectos analizados:** {comparison['total_projects']}
**Fecha:** {comparison['timestamp']}

---

## 📈 Resumen General

- **Total de archivos:** {comparison['summary']['total_files']:,}
- **Tamaño total:** {comparison['summary']['total_size_human']}
- **Puntuación promedio de salud:** {comparison['summary']['average_health_score']} ({comparison['summary']['average_health_grade']})
- **Mejor proyecto:** {comparison['summary']['best_project']}

"""
        
        if comparison['summary']['needs_attention']:
            md += f"""### ⚠️ Proyectos que requieren atención

Los siguientes proyectos tienen una puntuación de salud menor a 70:

"""
            for project in comparison['summary']['needs_attention']:
                md += f"- {project}\n"
            md += "\n"
        
        md += "---\n\n## 🎯 Análisis por Proyecto\n\n"
        
        # Ordenar proyectos por score de salud (descendente)
        projects = sorted(comparison['projects'], key=lambda x: x['health']['score'], reverse=True)
        
        for i, project in enumerate(projects, 1):
            md += f"### {i}. {project['name']}\n\n"
            md += f"**Ruta:** `{project['path']}`\n\n"
            
            # Score de salud con emoji
            score = project['health']['score']
            emoji = '🟢' if score >= 80 else '🟡' if score >= 60 else '🔴'
            md += f"**Puntuación de Salud:** {emoji} {score}/100 - {project['health']['grade']}\n\n"
            
            # Métricas
            md += "#### Métricas\n\n"
            md += f"- **Archivos totales:** {project['metrics']['files']:,}\n"
            md += f"- **Tamaño:** {project['metrics']['size']}\n"
            md += f"- **Tecnologías:** {', '.join(project['metrics']['technologies']) if project['metrics']['technologies'] else 'No detectadas'}\n"
            md += f"- **Grupos de dependencias:** {project['metrics']['dependencies_groups']}\n"
            md += f"- **Archivos de código:** {project['metrics']['code_files']}\n"
            md += f"- **Archivos de configuración:** {project['metrics']['config_files']}\n"
            md += f"- **Archivos de documentación:** {project['metrics']['doc_files']}\n\n"
            
            # Factores de salud
            md += "#### Factores de Salud\n\n"
            for factor, description in project['health']['factors'].items():
                icon = '✅' if '(0)' in description or '(+' in description else '⚠️'
                md += f"- {icon} **{factor.replace('_', ' ').title()}:** {description}\n"
            md += "\n"
            
            # Recomendaciones principales
            if project['top_recommendations']:
                md += "#### Recomendaciones Principales\n\n"
                for rec in project['top_recommendations']:
                    md += f"- {rec}\n"
                md += "\n"
            
            md += "---\n\n"
        
        return md
    
    def export_metrics_for_monitoring(self, output_path: str):
        """Exporta métricas en formato para sistemas de monitoreo"""
        metrics = []
        
        for analysis in self.analyses:
            health = self.calculate_health_score(analysis)
            
            metric = {
                'timestamp': analysis.timestamp,
                'project': analysis.project_name,
                'metrics': {
                    'health_score': health['score'],
                    'file_count': analysis.file_count,
                    'total_size_bytes': analysis.total_size,
                    'technology_count': len(analysis.technologies),
                    'dependency_groups': len(analysis.dependencies),
                    'recommendation_count': len(analysis.recommendations),
                    'code_to_config_ratio': (
                        analysis.metrics.get('code_files', 0) / 
                        max(analysis.metrics.get('config_files', 1), 1)
                    )
                },
                'tags': {
                    'technologies': analysis.technologies,
                    'grade': health['grade']
                }
            }
            
            metrics.append(metric)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(metrics, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Métricas exportadas a: {output_path}")


def example_1_compare_projects():
    """Ejemplo 1: Comparar múltiples proyectos"""
    print("=" * 70)
    print("📊 EJEMPLO 1: Análisis Comparativo de Proyectos")
    print("=" * 70)
    print()
    
    # Proyectos a analizar (ajusta estas rutas)
    projects = [
        '.',  # Proyecto actual
        # '/ruta/a/proyecto1',
        # '/ruta/a/proyecto2',
    ]
    
    analyzer = AdvancedAnalyzer()
    analyzer.analyze_projects(projects)
    
    # Generar reporte comparativo
    comparison = analyzer.generate_comparison_report()
    
    # Mostrar resumen
    print("\n" + "=" * 70)
    print("📈 RESUMEN COMPARATIVO")
    print("=" * 70)
    print(f"Proyectos analizados: {comparison['total_projects']}")
    print(f"Salud promedio: {comparison['summary']['average_health_score']}/100")
    print(f"Mejor proyecto: {comparison['summary']['best_project']}")
    
    # Exportar reportes
    md_report = analyzer.generate_markdown_comparison(comparison)
    with open('comparacion_proyectos.md', 'w', encoding='utf-8') as f:
        f.write(md_report)
    print("\n✅ Reporte guardado en: comparacion_proyectos.md")
    
    # Exportar métricas
    analyzer.export_metrics_for_monitoring('metrics_export.json')


def example_2_health_monitoring():
    """Ejemplo 2: Monitoreo de salud de un proyecto"""
    print("\n" + "=" * 70)
    print("🏥 EJEMPLO 2: Monitoreo de Salud del Proyecto")
    print("=" * 70)
    print()
    
    agent = ProjectResourceAgent('.')
    analysis = agent.analyze()
    
    analyzer = AdvancedAnalyzer()
    health = analyzer.calculate_health_score(analysis)
    
    print(f"Proyecto: {analysis.project_name}")
    print(f"Puntuación de Salud: {health['score']}/100")
    print(f"Calificación: {health['grade']}")
    print(f"\nFactores evaluados:")
    
    for factor, description in health['factors'].items():
        print(f"  - {factor.replace('_', ' ').title()}: {description}")
    
    # Determinar acciones
    print(f"\n{'=' * 70}")
    if health['score'] >= 80:
        print("✅ El proyecto está en buen estado!")
    elif health['score'] >= 60:
        print("⚠️  El proyecto necesita algunas mejoras")
    else:
        print("🚨 El proyecto requiere atención urgente")


def example_3_trend_analysis():
    """Ejemplo 3: Análisis de tendencias (requiere múltiples análisis en el tiempo)"""
    print("\n" + "=" * 70)
    print("📈 EJEMPLO 3: Análisis de Tendencias")
    print("=" * 70)
    print()
    
    print("Para análisis de tendencias:")
    print("1. Ejecuta el análisis periódicamente (ej. semanalmente)")
    print("2. Guarda los resultados con timestamp")
    print("3. Compara los resultados en el tiempo")
    print()
    print("Ejemplo de script para cron:")
    print("""
# Análisis semanal
0 9 * * 1 cd /proyecto && python3 project_resource_agent.py . \\
    -f json -o "analisis_$(date +\\%Y\\%m\\%d).json"
    """)


def main():
    """Ejecuta los ejemplos avanzados"""
    print("=" * 70)
    print("🚀 EJEMPLOS AVANZADOS - AGENTE DE ANÁLISIS DE RECURSOS")
    print("=" * 70)
    print()
    
    # Ejecutar ejemplos
    example_1_compare_projects()
    example_2_health_monitoring()
    example_3_trend_analysis()
    
    print("\n" + "=" * 70)
    print("✨ Ejemplos completados!")
    print("=" * 70)


if __name__ == '__main__':
    main()
