pipeline {
  agent any
  stages {
    stage('Checkout'){ steps{ checkout scm } }
    stage('Setup Python'){ steps{ sh 'python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt' } }
    stage('Lint'){ steps{ sh '. .venv/bin/activate && flake8' } }
    stage('Test'){ steps{ sh '. .venv/bin/activate && pytest -q' } }
    stage('Bandit'){ steps{ sh '. .venv/bin/activate && bandit -r projects -q || true' } }
  }
}
