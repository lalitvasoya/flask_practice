pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                echo 'Building the ml backend application!'
                sh 'cd $WORKSPACE/application'
                sh 'docker-compose up --build'
            }
        }
        stage("test"){
            steps {
                echo 'Tesing the application!'
                echo 'Tested!'
            }
        }
        stage("deploy"){
            steps {
                echo 'Deploying the application!'
            }
        }
    }
}
