pipeline {
    agent any

    stages {
        stage('Verify Docker') {
            steps {
                script {
                    echo 'Checking Docker version...'
                    bat 'docker --version'
                }
            }
        }
    }
}
