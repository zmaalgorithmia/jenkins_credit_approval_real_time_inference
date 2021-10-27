pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        // ALGORITHMIA_DOMAIN = 'algosales.productionize.ai'
        ALGORITHMIA_DOMAIN = 'algorithmia.com'
        GIT_CONFIG_NOSYSTEM = '1'
        PYTHONUNBUFFERED = '1'
    }
    stages {
        stage('Build') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']],
                userRemoteConfigs: [[url: 'https://github.com/zmaalgorithmia/jenkins_credit_approval_real_time_inference.git']]])
            }
        }
        stage('Deploy') {
            steps {
                // use a python environment with: algorithmia>=1.2.0, gitpython>=2.1.0, six>=1.12.0
                withPythonEnv('Python-3.9') {
                    sh 'pip install -r requirements.txt'
                    sh 'python model_deploy.py'
                }
            }
        }
    }
}
