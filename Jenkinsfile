pipeline {
    agent any
    stages {
        stage('bwacreate') {
            agent { docker {image sushantpande/bwaefs:efs}
            }
            steps {
                sh 'echo JITENDRA'
                //sh 'export KUBECONFIG=/root/.kube/kind-config-kind && kubectl apply -f /tmp/bwapod.yaml'
                //sh 'kubectl apply -f /tmp/bwapod.yaml'
            }
        }
/*
        stage('bwaexec'){
            steps {
                //sh 'export KUBECONFIG=/root/.kube/kind-config-kind && POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R {{ params.meta }} /tmp/scaffolds.fasta /tmp/evolved-6-R1.fastq | samtools sort > /tmp/bwaoutput.bam && samtools index /tmp/bwaoutput.bam && exit" && kubectl delete -n default deployment bwa-deployment'
                sh 'POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R {{ params.meta }} /tmp/scaffolds.fasta /tmp/evolved-6-R1.fastq | samtools sort > /tmp/bwaoutput.bam && samtools index /tmp/bwaoutput.bam && exit" && kubectl delete -n default deployment bwa-deployment'
            }
        }
        stage('gatkcreate'){
            agent none
            steps {
                sh 'export KUBECONFIG=/root/.kube/kind-config-kind && kubectl apply -f /tmp/gatkpod.yaml'
            }
        }
        stage('gatkexec'){
            agent none
            steps {
                sh 'export KUBECONFIG=/root/.kube/kind-config-kind && POD=$(kubectl get pod -l app=gatkapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "gatk HaplotypeCaller -R /tmp/scaffolds.fasta -I /tmp/bwaoutput.bam -O /tmp/gatkoutput.vcf" && kubectl delete -n default deployment gatk-deployment'
            }
        }
*/
    }
}
