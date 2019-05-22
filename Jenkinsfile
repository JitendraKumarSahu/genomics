pipeline {
   environment {
       didSucceed = true
   }
   agent any
      /*
      parameters {
         string(name: 'bwamem' , defaultValue: '@RG\\tID:foo\\tLB:bar\\tPL:illumina\\tPU:illumina\\tSM:SAMPLE', description: 'bwa mem parameters')
      }
      */
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
           steps {
              script {
                 if (env.taskResultStageA == 'true') {
                    sh "echo ${env.taskIDStageA}"
                    sh "echo ${env.taskResultStageA}"
                    sh 'POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R "@RG\\tID:foo\\tLB:bar\\tPL:illumina\\tPU:illumina\\tSM:SAMPLE\" /mnt/efs/scaffolds.fasta /mnt/efs/evolved-6-R1.fastq | samtools sort > /mnt/efs/bwaoutput.bam && samtools index /mnt/efs/bwaoutput.bam" && exit'
                    env.taskIDStageB = 1
                    env.taskResultStageB = true
                    sh "echo ${env.taskIDStageB}"
                    sh "echo ${env.taskResultStageB}"
                 } else {
                    env.taskIDStageB = 0
                    env.taskResultStageB = false
                 }
              }
              sh "echo ${env.taskIDStageB}"
              sh "echo ${env.taskResultStageB}"
           }
        }
       /*
        stage('gatkcreate'){
            steps {
               script {
                  if (env.taskResultStageB == 'true') {
                      sh 'whoami && kubectl apply -f /tmp/gatkpod.yaml'
                      def str1 = sh(script: 'kubectl get deployment -l app=gatkapp -o jsonpath="{.items[0].metadata.name}"', returnStdout: true)
                      echo "${str1}"
                      if ( str1.equals("gatk-deployment")) {
                          env.taskIDStageC = 1
                          env.taskResultStageC = true
                      } else {
                          env.taskIDStageC = 0
                          env.taskResultStageC = false
                      }
                  } else {
                      env.taskIDStageC = 0
                      env.taskResultStageC = false
                  }
               }
               sh "echo ${env.taskIDStageA}"
               sh "echo ${env.taskResultStageA}"
            }
        }
       
        stage('gatkexec'){
            steps {
              script {
                 if (env.taskResultStageC == 'true') {
                    sh "echo ${env.taskIDStageC}"
                    sh "echo ${env.taskResultStageC}"
                    sh 'POD=$(kubectl get pod -l app=gatkapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "gatk HaplotypeCaller -R /mnt/efs/scaffolds.fasta -I /mnt/efs/bwaoutput.bam -O /mnt/efs/gatkoutput.vcf" '  
                    env.taskIDStageD = 1
                    env.taskResultStageD = true
                    sh "echo ${env.taskIDStageD}"
                    sh "echo ${env.taskResultStageD}"
                 } else {
                    env.taskIDStageD = 0
                    env.taskResultStageD = false
                 }
              }
              sh "echo ${env.taskIDStageD}"
              sh "echo ${env.taskResultStageD}"
           }
        }
        
    }
}
*/
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
