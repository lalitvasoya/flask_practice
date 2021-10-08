pipeline {
    agent { label 'slave1'}
    environment {
        JENKINS_GIT_LTS_BRANCH = 'feature/master_slave'
    }
    stages {
        stage("Pull jenkins script") {
            steps {
                git(
                    branch: "${JENKINS_GIT_LTS_BRANCH}",
                    credentialsId: 'git-cred',
                    url: 'https://github.com/lalitvasoya/jenkins.git'
                )
                checkout scm
            }
        }
        stage("BUILD") {
            steps {
                sh 'bash ${WORKSPACE}/jenkins/script/build.sh'
            }
        }
        stage("CHECK-linting") {
            steps {
                echo "Linting"
                sh 'bash ${WORKSPACE}/jenkins/script/check_linting.sh'
            }
        }
        stage("TEST"){
            steps {
                echo "Testing"
                sh 'bash ${WORKSPACE}/jenkins/script/test.sh'
            }
        }
        stage("Deploy"){
            when {
                expression { sha1 == 'develop'}
            }
            steps{
                echo "-----------${sha1}----------------"
                withCredentials([
                    usernamePassword(credentialsId: 'git-cred', usernameVariable: 'GITHUB_USERNAME', passwordVariable: 'GITHUB_PASSWORD'),
                    sshUserPrivateKey(credentialsId: 'connect-key', keyFileVariable: 'KEY')
                    ]){
                    sh 'echo "$GITHUB_USERNAME $GITHUB_PASSWORD $GIT_LOCAL_BRANCH"'               
                    sh 'bash ${WORKSPACE}/jenkins/deploy.sh $GITHUB_USERNAME $GITHUB_PASSWORD $KEY'
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
