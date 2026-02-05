# 🚀 Plantillas CI/CD para el Agente de Análisis de Recursos

## GitHub Actions

### Análisis en cada Pull Request

```yaml
# .github/workflows/project-analysis.yml
name: Project Analysis

on:
  pull_request:
    branches: [ main, develop ]
  push:
    branches: [ main ]

jobs:
  analyze:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Download Project Resource Agent
      run: |
        curl -O https://raw.githubusercontent.com/your-repo/project_resource_agent.py
        chmod +x project_resource_agent.py
    
    - name: Run Project Analysis
      run: |
        python3 project_resource_agent.py . --format json --output analysis.json
    
    - name: Generate Report
      run: |
        python3 project_resource_agent.py . --format markdown --output ANALYSIS_REPORT.md
    
    - name: Upload Analysis Report
      uses: actions/upload-artifact@v3
      with:
        name: project-analysis
        path: |
          analysis.json
          ANALYSIS_REPORT.md
    
    - name: Comment PR with Summary
      if: github.event_name == 'pull_request'
      uses: actions/github-script@v6
      with:
        script: |
          const fs = require('fs');
          const analysis = JSON.parse(fs.readFileSync('analysis.json', 'utf8'));
          
          const comment = `## 📊 Project Analysis Results
          
          - **Total Files:** ${analysis.file_count}
          - **Project Size:** ${analysis.metrics.total_size_human}
          - **Technologies:** ${analysis.technologies.join(', ')}
          - **Health Recommendations:** ${analysis.recommendations.length}
          
          <details>
          <summary>View Recommendations</summary>
          
          ${analysis.recommendations.map((r, i) => `${i+1}. ${r}`).join('\n')}
          
          </details>
          `;
          
          github.rest.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: comment
          });
```

### Análisis Periódico Automatizado

```yaml
# .github/workflows/weekly-analysis.yml
name: Weekly Project Analysis

on:
  schedule:
    # Ejecutar cada lunes a las 9:00 AM
    - cron: '0 9 * * 1'
  workflow_dispatch:  # Permitir ejecución manual

jobs:
  weekly-analysis:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Download Agent
      run: |
        curl -O https://example.com/project_resource_agent.py
        chmod +x project_resource_agent.py
    
    - name: Run Analysis
      run: |
        DATE=$(date +%Y-%m-%d)
        python3 project_resource_agent.py . -f html -o "analysis_$DATE.html"
        python3 project_resource_agent.py . -f json -o "analysis_$DATE.json"
    
    - name: Create Release with Reports
      uses: softprops/action-gh-release@v1
      with:
        tag_name: analysis-${{ github.run_number }}
        name: Weekly Analysis Report
        files: |
          analysis_*.html
          analysis_*.json
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## GitLab CI

### Pipeline Completo

```yaml
# .gitlab-ci.yml
stages:
  - analyze
  - report
  - deploy

variables:
  AGENT_URL: "https://example.com/project_resource_agent.py"

before_script:
  - apt-get update -qq
  - apt-get install -y python3 python3-pip curl

analyze_project:
  stage: analyze
  image: python:3.11-slim
  script:
    - curl -O $AGENT_URL
    - chmod +x project_resource_agent.py
    - python3 project_resource_agent.py . --format json --output analysis.json
    - python3 project_resource_agent.py . --format html --output analysis.html
  artifacts:
    paths:
      - analysis.json
      - analysis.html
    expire_in: 30 days
  only:
    - main
    - develop
    - merge_requests

generate_report:
  stage: report
  image: python:3.11-slim
  dependencies:
    - analyze_project
  script:
    - curl -O $AGENT_URL
    - python3 project_resource_agent.py . --format markdown --output REPORT.md
    - cat REPORT.md
  artifacts:
    reports:
      markdown: REPORT.md
  only:
    - main
    - develop

pages:
  stage: deploy
  dependencies:
    - analyze_project
  script:
    - mkdir -p public
    - cp analysis.html public/index.html
  artifacts:
    paths:
      - public
  only:
    - main
```

## Jenkins

### Jenkinsfile

```groovy
pipeline {
    agent any
    
    environment {
        AGENT_URL = 'https://example.com/project_resource_agent.py'
    }
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    curl -O ${AGENT_URL}
                    chmod +x project_resource_agent.py
                '''
            }
        }
        
        stage('Analyze Project') {
            steps {
                sh '''
                    python3 project_resource_agent.py . \
                        --format json \
                        --output analysis-${BUILD_NUMBER}.json
                    
                    python3 project_resource_agent.py . \
                        --format html \
                        --output analysis-${BUILD_NUMBER}.html
                '''
            }
        }
        
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'analysis-*.json,analysis-*.html',
                                fingerprint: true
                
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: "analysis-${BUILD_NUMBER}.html",
                    reportName: 'Project Analysis Report'
                ])
            }
        }
        
        stage('Check Health') {
            steps {
                script {
                    def analysis = readJSON file: "analysis-${BUILD_NUMBER}.json"
                    def recCount = analysis.recommendations.size()
                    
                    if (recCount > 10) {
                        unstable(message: "Project has ${recCount} recommendations")
                    }
                    
                    echo "Analysis complete: ${analysis.file_count} files analyzed"
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Analysis completed successfully!'
        }
        failure {
            echo 'Analysis failed!'
        }
    }
}
```

## CircleCI

### Config

```yaml
# .circleci/config.yml
version: 2.1

jobs:
  analyze:
    docker:
      - image: python:3.11
    steps:
      - checkout
      
      - run:
          name: Download Agent
          command: |
            curl -O https://example.com/project_resource_agent.py
            chmod +x project_resource_agent.py
      
      - run:
          name: Analyze Project
          command: |
            python3 project_resource_agent.py . -f json -o analysis.json
            python3 project_resource_agent.py . -f html -o analysis.html
      
      - store_artifacts:
          path: analysis.json
          destination: reports/analysis.json
      
      - store_artifacts:
          path: analysis.html
          destination: reports/analysis.html
      
      - persist_to_workspace:
          root: .
          paths:
            - analysis.json

  report:
    docker:
      - image: python:3.11
    steps:
      - checkout
      
      - attach_workspace:
          at: .
      
      - run:
          name: Generate Report Summary
          command: |
            python3 -c "
            import json
            with open('analysis.json') as f:
                data = json.load(f)
            print(f'Files: {data[\"file_count\"]}')
            print(f'Size: {data[\"metrics\"][\"total_size_human\"]}')
            print(f'Technologies: {len(data[\"technologies\"])}')
            "

workflows:
  version: 2
  analyze-project:
    jobs:
      - analyze
      - report:
          requires:
            - analyze
  
  weekly-analysis:
    triggers:
      - schedule:
          cron: "0 9 * * 1"
          filters:
            branches:
              only:
                - main
    jobs:
      - analyze
```

## Azure Pipelines

### Pipeline YAML

```yaml
# azure-pipelines.yml
trigger:
  - main
  - develop

pool:
  vmImage: 'ubuntu-latest'

variables:
  agentUrl: 'https://example.com/project_resource_agent.py'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.11'
  displayName: 'Use Python 3.11'

- script: |
    curl -O $(agentUrl)
    chmod +x project_resource_agent.py
  displayName: 'Download Project Agent'

- script: |
    python3 project_resource_agent.py . --format json --output $(Build.ArtifactStagingDirectory)/analysis.json
    python3 project_resource_agent.py . --format html --output $(Build.ArtifactStagingDirectory)/analysis.html
  displayName: 'Analyze Project'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'project-analysis'
    publishLocation: 'Container'
  displayName: 'Publish Analysis Reports'

- script: |
    python3 -c "
    import json
    with open('$(Build.ArtifactStagingDirectory)/analysis.json') as f:
        data = json.load(f)
    print(f'##vso[task.setvariable variable=FileCount]{data[\"file_count\"]}')
    print(f'##vso[task.setvariable variable=TechCount]{len(data[\"technologies\"])}')
    "
  displayName: 'Extract Metrics'

- script: |
    echo "Project analyzed: $(FileCount) files"
    echo "Technologies detected: $(TechCount)"
  displayName: 'Display Summary'
```

## Travis CI

### Configuration

```yaml
# .travis.yml
language: python
python:
  - "3.11"

cache:
  directories:
    - $HOME/.cache/pip

before_script:
  - curl -O https://example.com/project_resource_agent.py
  - chmod +x project_resource_agent.py

script:
  - python3 project_resource_agent.py . --format json --output analysis.json
  - python3 project_resource_agent.py . --format html --output analysis.html

after_success:
  - |
    if [ "$TRAVIS_BRANCH" == "main" ]; then
      python3 project_resource_agent.py . --format markdown --output ANALYSIS.md
    fi

deploy:
  provider: pages
  skip_cleanup: true
  github_token: $GITHUB_TOKEN
  local_dir: .
  on:
    branch: main
```

## Bitbucket Pipelines

### Configuration

```yaml
# bitbucket-pipelines.yml
image: python:3.11

pipelines:
  default:
    - step:
        name: Project Analysis
        caches:
          - pip
        script:
          - curl -O https://example.com/project_resource_agent.py
          - chmod +x project_resource_agent.py
          - python3 project_resource_agent.py . -f json -o analysis.json
          - python3 project_resource_agent.py . -f html -o analysis.html
        artifacts:
          - analysis.json
          - analysis.html
  
  branches:
    main:
      - step:
          name: Full Analysis
          script:
            - curl -O https://example.com/project_resource_agent.py
            - python3 project_resource_agent.py . -f json -o analysis.json
            - python3 project_resource_agent.py . -f html -o analysis.html
            - python3 project_resource_agent.py . -f markdown -o REPORT.md
          artifacts:
            - analysis.json
            - analysis.html
            - REPORT.md
  
  custom:
    weekly-report:
      - step:
          name: Weekly Analysis Report
          script:
            - curl -O https://example.com/project_resource_agent.py
            - DATE=$(date +%Y-%m-%d)
            - python3 project_resource_agent.py . -f html -o "weekly_report_$DATE.html"
          artifacts:
            - weekly_report_*.html
```

## Docker Integration

### Dockerfile para el Agente

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY project_resource_agent.py .

RUN chmod +x project_resource_agent.py

ENTRYPOINT ["python3", "project_resource_agent.py"]
CMD ["."]
```

### Docker Compose para Análisis

```yaml
# docker-compose.analysis.yml
version: '3.8'

services:
  analyzer:
    build:
      context: .
      dockerfile: Dockerfile.analyzer
    volumes:
      - ./project:/project:ro
      - ./reports:/reports
    command: ["/project", "-f", "html", "-o", "/reports/analysis.html"]
```

### Uso con Docker

```bash
# Construir imagen
docker build -t project-analyzer -f Dockerfile.analyzer .

# Analizar proyecto
docker run --rm \
  -v $(pwd):/project:ro \
  -v $(pwd)/reports:/reports \
  project-analyzer /project -f html -o /reports/analysis.html

# Con Docker Compose
docker-compose -f docker-compose.analysis.yml up
```

## Integración con Pre-commit Hooks

### Pre-commit Config

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: project-analysis
        name: Project Analysis
        entry: python3 project_resource_agent.py
        args: ['.', '-f', 'json', '-o', '.project_analysis.json']
        language: system
        pass_filenames: false
        always_run: true
```

### Git Hook Manual

```bash
#!/bin/bash
# .git/hooks/pre-push

echo "Running project analysis..."

python3 project_resource_agent.py . -f json -o .analysis_cache.json

# Verificar el número de recomendaciones
REC_COUNT=$(python3 -c "import json; data = json.load(open('.analysis_cache.json')); print(len(data['recommendations']))")

if [ "$REC_COUNT" -gt 15 ]; then
  echo "Warning: Project has $REC_COUNT recommendations"
  echo "Consider addressing some before pushing"
  read -p "Continue anyway? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
  fi
fi

exit 0
```

## Makefile Integration

```makefile
# Makefile
.PHONY: analyze analyze-json analyze-html analyze-md report clean

AGENT_SCRIPT = project_resource_agent.py
TIMESTAMP = $(shell date +%Y%m%d_%H%M%S)

analyze: analyze-json analyze-html analyze-md
	@echo "✅ Analysis complete! Check reports/ directory"

analyze-json:
	@mkdir -p reports
	python3 $(AGENT_SCRIPT) . -f json -o reports/analysis_$(TIMESTAMP).json

analyze-html:
	@mkdir -p reports
	python3 $(AGENT_SCRIPT) . -f html -o reports/analysis_$(TIMESTAMP).html

analyze-md:
	@mkdir -p reports
	python3 $(AGENT_SCRIPT) . -f markdown -o reports/analysis_$(TIMESTAMP).md

report: analyze-html
	@open reports/analysis_$(TIMESTAMP).html || xdg-open reports/analysis_$(TIMESTAMP).html

clean:
	rm -rf reports/*.json reports/*.html reports/*.md

latest:
	@ls -t reports/analysis_*.html | head -1 | xargs open || xdg-open
```

## NPM Scripts Integration

```json
{
  "scripts": {
    "analyze": "python3 project_resource_agent.py . -f html -o reports/analysis.html",
    "analyze:json": "python3 project_resource_agent.py . -f json -o reports/analysis.json",
    "analyze:watch": "watch 'npm run analyze' src/",
    "precommit": "python3 project_resource_agent.py . -f json -o .analysis.json",
    "report": "python3 project_resource_agent.py . -f html -o reports/report.html && open reports/report.html"
  }
}
```

---

## Tips para Integración

1. **Almacena el agente en tu repositorio**: Copia `project_resource_agent.py` a tu repo para garantizar disponibilidad
2. **Versioná los reportes**: Usa timestamps o números de build
3. **Configura límites**: Define cuándo un análisis debe fallar (ej. > 20 recomendaciones)
4. **Cachea dependencias**: En CI/CD, cachea Python y dependencias
5. **Usa artifacts**: Siempre guarda los reportes como artifacts
6. **Automatiza notificaciones**: Envía reportes por email/Slack
7. **Dashboard centralizado**: Agrega links a los reportes en tu wiki/dashboard

## Monitoreo Continuo

```bash
# Script para análisis continuo
#!/bin/bash

while true; do
  python3 project_resource_agent.py . -f json -o /tmp/current_analysis.json
  
  # Enviar métricas a sistema de monitoreo
  curl -X POST https://metrics.example.com/api/ingest \
    -H "Content-Type: application/json" \
    -d @/tmp/current_analysis.json
  
  sleep 3600  # Cada hora
done
```
