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
                withCredentials([usernamePassword(credentialsId: 'git-cred', usernameVariable: 'GITHUB_USERNAME', passwordVariable: 'GITHUB_PASSWORD')]){
                    sh 'echo "$GITHUB_USERNAME $GITHUB_PASSWORD $GIT_LOCAL_BRANCH"'               
                    sh '/script/deploy.sh $GITHUB_USERNAME $GITHUB_PASSWORD'
                }
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
