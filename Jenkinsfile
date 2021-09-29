pipeline {
    agent any
    stages {
        stage("BUILD") {
            steps {
                sh '/script/build.sh'
            }
        }
        stage("CHECK-linting") {
            steps {
                echo "Linting"
                // sh '/script/check_linting.sh'
            }
        }
        stage("TEST"){
            steps {
                echo "Testing"
                // sh '/script/check_linting.sh'
            }
        }
        stage("Deploy"){
            steps{
                sh '/script/deploy.sh'
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
