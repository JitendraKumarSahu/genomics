pipeline {
    agent none
    stages {
        stage('bwaapp') {
            agent {
                docker { image 'sushantpande/bwaefs:efs' }
            }
            steps {
                sh 'mkdir /mnt/efs && mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=300,retrans=1,noresvport 172.31.42.102:/ /mnt/efs && while true; do sleep 30; done;'
            }
        }
    }
}
