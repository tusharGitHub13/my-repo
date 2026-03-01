pipeline {
  agent any
  stages {
    stage('Build') {
      steps { sh 'docker build -t my-python-app .' }
    }
    stage('Test') {
      steps { sh 'echo "Add pytest here  "' }
    }
    stage('Deploy') {
      steps { sh 'docker run -d -p 5000:5000 my-python-app' }
    }
  }
}
