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
                sh '/script/check_linting.sh'
            }
        }
        stage("TEST"){
            steps {
                echo "Testing"
                sh '/script/check_linting.sh'
            }
        }
        stage("Deploy"){
            when {
                expression {
                    return env.BRANCH_NAME != 'master';
                }
            }
            steps{
                echo "-----------${env.GITHUB_PR_STATE}----------------"
                echo "-----------${env.GITHUB_PR_TARGET_BRANCH}----------------"
                echo "-----------${env.BRANCH_NAME}----------------"
                withCredentials([usernamePassword(credentialsId: 'git-cred', usernameVariable: 'GITHUB_USERNAME', passwordVariable: 'GITHUB_PASSWORD')]){
                    sh 'echo "$GITHUB_USERNAME $GITHUB_PASSWORD $GIT_LOCAL_BRANCH"'               
                    sh 'bash /script/deploy.sh $GITHUB_USERNAME $GITHUB_PASSWORD'
                }
            }
        }
    }
    post{
        always{
            echo 'Docker stop application'
            sh 'docker stop flask-practice'
            notificationSend()
            googleChatNotifation()
        }
    }
}

def notificationSend(){
    emailext (
        attachLog: true,
        subject: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
        body: """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
            <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
        recipientProviders: [developers(), buildUser()],
        to: "${env.ghprbActualCommitAuthorEmail}"
    )
}

def googleChatNotifation(){
    googlechatnotification(
        url: "id:google-chat",
        message: "${env.JOB_NAME} Done ${env.JOB_NAME}: ${env.BUILD_NUMBER} url: ${env.BUILD_URL}",
        sameThreadNotification: true
    )
}
