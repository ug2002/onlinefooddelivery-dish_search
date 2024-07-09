pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ug2002/onlinefooddelivery-dish_search:latest'
        REPOSITORY_URL = 'https://github.com/ug2002/onlinefooddelivery-dish_search.git'
        GIT_CREDENTIALS_ID = 'github-credentials'
        SLACK_CHANNEL = '#build-notifications'
        SLACK_CREDENTIALS_ID = 'slack-credentials-id'
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

        stage('Build') {
            steps {
                script {
                    echo 'Building Docker image...'
                    sh '''
                    docker build -t ${DOCKER_IMAGE} .
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh '''
                    pip install -r requirements.txt
                    pytest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying Docker image...'
                    sh '''
                    docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
                    docker push ${DOCKER_IMAGE}
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
                    slackSend channel: "${SLACK_CHANNEL}", message: "Build status: ${currentBuild.currentResult}", teamDomain: 'your-slack-team', tokenCredentialId: "${SLACK_CREDENTIALS_ID}"
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Build succeeded!'
                slackSend channel: "${SLACK_CHANNEL}", message: "Build succeeded: ${env.BUILD_URL}", teamDomain: 'your-slack-team', tokenCredentialId: "${SLACK_CREDENTIALS_ID}"
            }
        }

        failure {
            script {
                echo 'Build failed!'
                slackSend channel: "${SLACK_CHANNEL}", message: "Build failed: ${env.BUILD_URL}", teamDomain: 'your-slack-team', tokenCredentialId: "${SLACK_CREDENTIALS_ID}"
            }
        }

        always {
            script {
                echo 'Cleaning up...'
                sh 'docker system prune -f'
            }
        }
    }
}
