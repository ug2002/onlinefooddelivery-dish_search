pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ug2002/onlinefooddelivery-dish_search:latest'
        REPOSITORY_URL = 'https://github.com/ug2002/onlinefooddelivery-dish_search.git'
        GIT_CREDENTIALS_ID = 'github-credentials'
        SLACK_CHANNEL = '#build-notifications'
        SLACK_CREDENTIALS_ID = 'slack-credentials-id'
        PYTHON_PATH = 'C:\\Python312'  // Updated path
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Checking out the source code...'
                    deleteDir()
                    git url: "${REPOSITORY_URL}", credentialsId: "${GIT_CREDENTIALS_ID}", branch: 'main'
                }
            }
        }

        stage('Verify Python') {
            steps {
                script {
                    echo 'Printing Python version...'
                    bat '"%PYTHON_PATH%\\python.exe" --version'

                    echo 'Printing pip version...'
                    bat '"%PYTHON_PATH%\\python.exe" -m pip --version'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Printing environment variables...'
                    bat 'set'

                    echo 'Printing Docker version...'
                    bat 'docker --version'

                    echo 'Building Docker image...'
                    bat '''
                    docker build -t %DOCKER_IMAGE% .
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    bat '"%PYTHON_PATH%\\python.exe" -m pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    bat '"%PYTHON_PATH%\\python.exe" -m pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying Docker image...'
                    bat '''
                    docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%
                    docker push %DOCKER_IMAGE%
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    '''
                }
            }
        }

        stage('Notify') {
            steps {
                script {
                    echo 'Sending Slack notifications...'
                    slackSend channel: "${SLACK_CHANNEL}", message: "Build status: ${currentBuild.currentResult}", tokenCredentialId: "${SLACK_CREDENTIALS_ID}"
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Build succeeded!'
                slackSend channel: "${SLACK_CHANNEL}", message: "Build succeeded: ${env.BUILD_URL}", tokenCredentialId: "${SLACK_CREDENTIALS_ID}"
            }
        }

        failure {
            script {
                echo 'Build failed!'
                slackSend channel: "${SLACK_CHANNEL}", message: "Build failed: ${env.BUILD_URL}", tokenCredentialId: "${SLACK_CREDENTIALS_ID}"
            }
        }

        always {
            script {
                echo 'Cleaning up...'
                bat 'docker system prune -f'
            }
        }
    }
}
