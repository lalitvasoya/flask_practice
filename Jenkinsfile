pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                echo 'Building the ml backend application!'
                sh '''
                    cd $WORKSPACE/application
                    docker-compose --build
                '''
            }
        }
        stage("deploy"){
            steps {
                echo 'docker-compose up -d!'
            }
        }
    }
}
