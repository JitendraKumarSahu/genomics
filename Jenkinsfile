pipeline {
    agent none
    stages {
        stage('bwaapp') {
            agent {
                docker { image 'sushantpande/bwaefs:efs' }
            }
        }
    }
}
