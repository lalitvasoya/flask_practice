pipeline {
    agent any
    stages {
        stage("BUILD") {
            steps {
                echo 'Docker build and up the application!'
                sh 'source /script/build.sh'
            }
        }
        stage("CHECK-linting") {
            steps {
                echo 'Check linting in the application!'
                sh 'source /script/check_linting.sh'
            }
        }
        stage("TEST"){
            steps {
                echo 'Testing the application'
                sh 'source /script/check_linting.sh'
            }
        }
    }
    post{
        always{
            echo 'Docker stop application'
            sh 'docker stop flask-practice'
        }
    }
}
