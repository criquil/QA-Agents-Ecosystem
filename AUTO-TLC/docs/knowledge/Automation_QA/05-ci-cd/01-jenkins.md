# Jenkins

> **Archivo:** 1 de 2 | **Sección:** CI/CD | **Nivel:** Avanzado

---

## Definición

**Jenkins** es el servidor de automatización open source más popular para CI/CD.

## Pipeline Example

### Jenkinsfile

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install') {
            steps {
                sh 'npm install'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        
        stage('Report') {
            steps {
                allure([
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        failure {
            mail to: 'team@example.com',
                 subject: "Build Failed: ${env.JOB_NAME}",
                 body: "Check: ${env.BUILD_URL}"
        }
    }
}
```

## Configuración

### Instalación

```bash
# Docker
docker run -p 8080:8080 jenkins/jenkins:lts

# macOS
brew install jenkins-lts
```

### Plugins Recomendados

```
- Allure Jenkins Plugin
- GitHub Pipeline
- Docker Pipeline
- Blue Ocean
```

## Resumen

- **Jenkins** es el estándar para CI/CD
- **Pipeline as Code** con Jenkinsfile
- **Plugins** para integración

---

## Navegación

- **Anterior:** [README.md](README.md)
- **Siguiente:** [02-github-actions.md](02-github-actions.md)
- **Volver a CI/CD:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 1 - Jenkins*
