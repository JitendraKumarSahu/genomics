pipeline {
   environment {
       didSucceed = true
   }
   agent any
      stages {
         stage ('bwacreate') {
            steps {
               script {
                  //sh "env"
                  sh "echo ${env.BUILD_ID}"
                  // sh "echo ${env.BUILD_NUMBER}"
                  sh 'export KUBECONFIG=/root/.kube/config && echo $KUBECONFIG && kubectl cluster-info'
                  sh 'whoami && echo $KUBECONFIG && kubectl apply -f /tmp/bwapod.yaml'
                  def str = sh(script: 'kubectl get deployment -l app=bwaapp -o jsonpath="{.items[0].metadata.name}"', returnStdout: true)
                  echo "${str}"
                  if ( str.equals("bwa-deployment")) {
                     env.taskIDStageA = 1
                     env.taskResultStageA = true
                  } else {
                     env.taskIDStageA = 0
                     env.taskResultStageA = false
                  }
                  
                }
               sh "echo ${env.taskIDStageA}"
               sh "echo ${env.taskResultStageA}"
            }
         }
         
        stage ('bwaexec') {
           when {
              expression{
                 return env.taskResultStageA == 'true';
              }   
           } 
           steps {
              sh "echo ${env.taskIDStageA}"
              sh "echo ${env.taskResultStageA}"
              sh 'POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R "@RG\\tID:foo\\tLB:bar\\tPL:illumina\\tPU:illumina\\tSM:SAMPLE" /mnt/efs/scaffolds.fasta /mnt/efs/evolved-6-R1.fastq | samtools sort > /mnt/efs/bwaoutput.bam && samtools index /mnt/efs/bwaoutput.bam" && exit'  
              env.taskIDStageB = 1
              env.taskResultStageB = true
              sh "echo ${env.taskIDStageb}"
              sh "echo ${env.taskResultStageB}"
           }
        }
       
        /*
        stage('gatkcreate'){
            steps {
                sh 'whoami'
                sh 'export KUBECONFIG=/root/.kube/config && kubectl apply -f /tmp/gatkpod.yaml'
            }
        }
       
        stage('gatkexec'){
            steps {
                sh 'whoami'
                sh 'export KUBECONFIG=/root/.kube/config && POD=$(kubectl get pod -l app=gatkapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "gatk HaplotypeCaller -R /mnt/efs/scaffolds.fasta -I /mnt/efs/bwaoutput.bam -O /mnt/efs/gatkoutput.vcf" '
            }
        }
        */
    }
}

/*
pipeline {
    agent any
    stages {
       
        stage('bwacreate') {
            steps {
                //sh 'export PATH=$PATH:/usr/local/go/bin'
                //sh 'export PATH=$PATH:$(go env GOPATH)/bin'
                //sh 'export KUBECONFIG="$(kind get kubeconfig-path --name="kind")"'
                //sh 'export KUBECONFIG=/root/.kube/config && echo $KUBECONFIG && kubectl cluster-info'
                //sh 'whoami && echo $KUBECONFIG && kubectl apply -f /tmp/bwapod.yaml'
                sh 'env'
            }
        }
        
        /* 
        stage('bwaexec'){
            steps {
                //sh whoami'
                sh 'POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R "@RG\\tID:foo\\tLB:bar\\tPL:illumina\\tPU:illumina\\tSM:SAMPLE" /mnt/efs/scaffolds.fasta /mnt/efs/evolved-6-R1.fastq | samtools sort > /mnt/efs/bwaoutput.bam && samtools index /mnt/efs/bwaoutput.bam" && exit'
                //sh 'POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R {{ params.meta }} /tmp/scaffolds.fasta /tmp/evolved-6-R1.fastq | samtools sort > /tmp/bwaoutput.bam && samtools index /tmp/bwaoutput.bam && exit" && kubectl delete -n default deployment bwa-deployment'
            }
        }
       
      
        stage('gatkcreate'){
            steps {
                sh 'whoami'
                sh 'export KUBECONFIG=/root/.kube/config && kubectl apply -f /tmp/gatkpod.yaml'
            }
        }
       
        stage('gatkexec'){
            steps {
                sh 'whoami'
                sh 'export KUBECONFIG=/root/.kube/config && POD=$(kubectl get pod -l app=gatkapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "gatk HaplotypeCaller -R /mnt/efs/scaffolds.fasta -I /mnt/efs/bwaoutput.bam -O /mnt/efs/gatkoutput.vcf" '
            }
        }
        
    }
}
*/
