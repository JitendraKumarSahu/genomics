pipeline {
    agent any
    stages {
        stage('bwacreate') {
            steps {
                //sh 'export PATH=$PATH:/usr/local/go/bin'
                //sh 'export PATH=$PATH:$(go env GOPATH)/bin'
                //sh 'export KUBECONFIG="$(kind get kubeconfig-path --name="kind")"'
                sh 'export KUBECONFIG=/ubuntu/.kube/config'
                sh 'whoami && echo $KUBECONFIG && kubectl apply -f /tmp/bwapod.yaml'
            }
        }
        /*
        stage('bwaexec'){
            steps {
                sh 'whoami'
                sh 'export KUBECONFIG=/root/.kube/kind-config-kind && POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R {{ params.meta }} /tmp/scaffolds.fasta /tmp/evolved-6-R1.fastq | samtools sort > /tmp/bwaoutput.bam && samtools index /tmp/bwaoutput.bam && exit" && kubectl delete -n default deployment bwa-deployment'
                //sh 'POD=$(kubectl get pod -l app=bwaapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "bwa mem -R {{ params.meta }} /tmp/scaffolds.fasta /tmp/evolved-6-R1.fastq | samtools sort > /tmp/bwaoutput.bam && samtools index /tmp/bwaoutput.bam && exit" && kubectl delete -n default deployment bwa-deployment'
            }
        }
        */
        /*
        stage('gatkcreate'){
            steps {
                sh 'whoami'
                sh 'export KUBECONFIG=/root/.kube/kind-config-kind && kubectl apply -f /tmp/gatkpod.yaml'
            }
        }
        stage('gatkexec'){
            steps {
                sh 'whoami'
                sh 'export KUBECONFIG=/root/.kube/kind-config-kind && POD=$(kubectl get pod -l app=gatkapp -o jsonpath="{.items[0].metadata.name}") && kubectl exec $POD -- /bin/bash -c "gatk HaplotypeCaller -R /tmp/scaffolds.fasta -I /tmp/bwaoutput.bam -O /tmp/gatkoutput.vcf" && kubectl delete -n default deployment gatk-deployment'
            }
        }
        */
    }
}
