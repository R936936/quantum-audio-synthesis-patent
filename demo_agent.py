#!/usr/bin/env python3
"""
Script de demostración del Agente Híbrido de Análisis de Recursos
Crea un proyecto de ejemplo y ejecuta el análisis
"""

import os
import tempfile
import shutil
from pathlib import Path
from project_resource_agent import ProjectResourceAgent


def create_demo_project():
    """Crea un proyecto de demostración"""
    # Crear directorio temporal
    demo_dir = Path(tempfile.mkdtemp(prefix='demo_project_'))
    
    print(f"🏗️  Creando proyecto de demostración en: {demo_dir}\n")
    
    # Crear estructura de directorios
    (demo_dir / 'src').mkdir()
    (demo_dir / 'tests').mkdir()
    (demo_dir / 'docs').mkdir()
    (demo_dir / 'config').mkdir()
    
    # Crear archivos de ejemplo
    files = {
        'README.md': """# Proyecto de Demostración

Este es un proyecto de ejemplo para demostrar las capacidades del agente.

## Características

- API REST con Flask
- Frontend con React
- Base de datos PostgreSQL
- Tests automatizados
- Dockerizado
""",
        'requirements.txt': """flask==2.3.0
flask-cors==4.0.0
psycopg2-binary==2.9.6
python-dotenv==1.0.0
pytest==7.3.1
pytest-cov==4.1.0
gunicorn==20.1.0
sqlalchemy==2.0.15
alembic==1.11.1
pydantic==1.10.8
""",
        'package.json': """{
  "name": "demo-project",
  "version": "1.0.0",
  "description": "Proyecto de demostración",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.4.0",
    "react-router-dom": "^6.11.0"
  },
  "devDependencies": {
    "react-scripts": "5.0.1",
    "@testing-library/react": "^13.4.0",
    "eslint": "^8.41.0"
  }
}
""",
        'Dockerfile': """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
""",
        'docker-compose.yml': """version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/demo
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=demo
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
""",
        '.gitignore': """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Node
node_modules/
npm-debug.log
yarn-error.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local
""",
        '.env.example': """DATABASE_URL=postgresql://user:password@localhost:5432/demo
SECRET_KEY=your-secret-key-here
DEBUG=True
PORT=8000
""",
        'src/app.py': """from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Demo API'})

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)
""",
        'src/models.py': """from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
""",
        'src/utils.py': """def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_response(data, status_code=200):
    return {'data': data, 'status': status_code}
""",
        'tests/test_app.py': """import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_health(client):
    response = client.get('/api/health')
    assert response.status_code == 200
""",
        'tests/test_utils.py': """from src.utils import validate_email, format_response

def test_validate_email():
    assert validate_email('test@example.com') == True
    assert validate_email('invalid-email') == False

def test_format_response():
    result = format_response({'key': 'value'}, 200)
    assert result['status'] == 200
    assert 'data' in result
""",
        'docs/API.md': """# API Documentation

## Endpoints

### GET /
Returns welcome message

### GET /api/health
Returns health status of the API
""",
        'config/settings.py': """import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DATABASE_URL = os.getenv('DATABASE_URL')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    PORT = int(os.getenv('PORT', 8000))
""",
        'Makefile': """install:
\tpip install -r requirements.txt

test:
\tpytest tests/ -v

run:
\tpython src/app.py

docker-build:
\tdocker-compose build

docker-up:
\tdocker-compose up -d

clean:
\tfind . -type d -name __pycache__ -exec rm -rf {} +
\tfind . -type f -name '*.pyc' -delete
""",
        'LICENSE': """MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
""",
    }
    
    # Escribir archivos
    for file_path, content in files.items():
        full_path = demo_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print("✅ Proyecto de demostración creado con:")
    print("   - Backend Flask (Python)")
    print("   - Frontend React (JavaScript)")
    print("   - Docker y Docker Compose")
    print("   - Tests con Pytest")
    print("   - Documentación")
    print("   - Configuración completa\n")
    
    return demo_dir


def main():
    """Función principal de demostración"""
    print("=" * 70)
    print("🤖 DEMOSTRACIÓN DEL AGENTE HÍBRIDO DE ANÁLISIS DE RECURSOS")
    print("=" * 70)
    print()
    
    # Crear proyecto de demostración
    demo_dir = create_demo_project()
    
    try:
        # Ejecutar análisis
        print("=" * 70)
        agent = ProjectResourceAgent(str(demo_dir))
        analysis = agent.analyze()
        
        # Generar reportes en diferentes formatos
        print("=" * 70)
        print("📝 Generando reportes en múltiples formatos...\n")
        
        # Reporte Markdown
        md_report = agent.generate_report(analysis, 'markdown')
        md_path = demo_dir / 'ANALISIS.md'
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_report)
        print(f"✅ Reporte Markdown: {md_path}")
        
        # Reporte JSON
        json_report = agent.generate_report(analysis, 'json')
        json_path = demo_dir / 'analisis.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(json_report)
        print(f"✅ Reporte JSON: {json_path}")
        
        # Reporte HTML
        html_report = agent.generate_report(analysis, 'html')
        html_path = demo_dir / 'analisis.html'
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_report)
        print(f"✅ Reporte HTML: {html_path}")
        
        print("\n" + "=" * 70)
        print("📊 RESUMEN DEL ANÁLISIS")
        print("=" * 70)
        print(f"📁 Proyecto: {analysis.project_name}")
        print(f"📄 Total de archivos: {analysis.file_count}")
        print(f"💾 Tamaño total: {analysis.metrics['total_size_human']}")
        print(f"🔧 Tecnologías: {', '.join(analysis.technologies)}")
        print(f"📦 Grupos de dependencias: {len(analysis.dependencies)}")
        print(f"🎯 Recursos clave: {len(analysis.resources)}")
        print(f"💡 Recomendaciones: {len(analysis.recommendations)}")
        
        print("\n" + "=" * 70)
        print("💡 RECOMENDACIONES PRINCIPALES")
        print("=" * 70)
        for i, rec in enumerate(analysis.recommendations[:5], 1):
            print(f"{i}. {rec}")
        
        print("\n" + "=" * 70)
        print("📋 RECURSOS POR CATEGORÍA")
        print("=" * 70)
        for category, count in analysis.metrics['resource_categories'].items():
            print(f"   {category.replace('_', ' ').title()}: {count} archivos")
        
        print("\n" + "=" * 70)
        print(f"✨ ¡Demostración completada! Reportes guardados en:\n   {demo_dir}")
        print("=" * 70)
        
        # Preguntar si desea ver el reporte Markdown
        print("\n¿Desea ver el reporte Markdown completo? (s/n): ", end='')
        try:
            response = input().strip().lower()
            if response == 's' or response == 'si' or response == 'y' or response == 'yes':
                print("\n" + "=" * 70)
                print(md_report)
                print("=" * 70)
        except (EOFError, KeyboardInterrupt):
            print()
        
        # Preguntar si desea eliminar el proyecto demo
        print("\n¿Desea eliminar el proyecto de demostración? (s/n): ", end='')
        try:
            response = input().strip().lower()
            if response == 's' or response == 'si' or response == 'y' or response == 'yes':
                shutil.rmtree(demo_dir)
                print(f"🗑️  Proyecto de demostración eliminado")
            else:
                print(f"📁 Proyecto de demostración conservado en: {demo_dir}")
        except (EOFError, KeyboardInterrupt):
            print(f"\n📁 Proyecto de demostración conservado en: {demo_dir}")
        
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")
        # Limpiar en caso de error
        if demo_dir.exists():
            shutil.rmtree(demo_dir)
        raise


if __name__ == '__main__':
    main()
