pipeline {
   environment {
       didSucceed = true
       /*
       AMQP_PORT =	15672	
       AMQP_PWD	 = "jenkins"	
       AMQP_SERVER = "172.31.33.249"	
       AMQP_USER = "jenkins"	
       REDIS_HOST = "172.31.33.249"	
       WORK_DIR_NAME = "tmp"    
       "bwa_gatk_dag_sleek.DATA_DIR" = "/mnt/efs"	
       "bwa_gatk_dag_sleek.bwa.input" = "evolved-6-R1.fastq"	
       "bwa_gatk_dag_sleek.bwa.split" =	1	
       "bwa_gatk_dag_sleek.bwa.split_size" = 0	
       "bwa_gatk_dag_sleek.bwa.yaml" = "/tmp/bwapodjob.yaml"
       "bwa_gatk_dag_sleek.gatk.yaml" = "/tmp/gatkpodjob.yaml"	
       "bwa_gatk_dag_sleek.max_cont" = 10	
       "bwa_gatk_dag_sleek.ref" = "scaffolds"	
       "bwa_gatk_dag_sleek.vcf.yaml" = "/tmp/vcfpodjob.yaml"
       */
   }
   agent any
    stages {
       
         stage ('bwa_cc') {
            steps {
               script {
                  /*
                  File f = new File("env.txt")
                  params.each {param ->
                       f.write("${param.key}"+"="+"${param.value}")
                  }
                  */
                  env.CURRENT_TASK = 'bwa_cc'
                  env.PARENT_TASK = null
                  def ti =  env.BUILD_ID +'_bwa_cc'
                  env.ti = ti
                  //sh 'echo "${BUILD_ID}_bwa_cc" >> env.ti'
                  sh "env >> env1.txt"
                  sh 'python3 create_cc.py env1.txt bwajob'
               }
            }
         }
        
        
        stage ('bwa_wait') {
           steps {
              script {
                 env.CURRENT_TASK = 'bwa_wait'
                 env.PARENT_TASK = 'bwa_cc'
                 def ti =  env.BUILD_ID +'_bwa_wait'
                 env.ti = ti
                 sh "env >> env2.txt"
                 sh "python3 noop.py env2.txt"
              }
           }
        }
        
        stage('gatk_cc'){
            steps {
               script {
                  env.CURRENT_TASK = 'gatk_cc'
                  env.PARENT_TASK = 'bwa_wait'
                  def ti =  env.BUILD_ID +'_gatk_cc'
                  env.ti = ti
                  sh "env >> env3.txt"
                  //sh 'python3 create_cc.py env3.txt gatkjob'
               }
            }
        }
       
       /*
        stage('gatk_wait'){
            steps {
              script {
                 env.CURRENT_TASK = 'gatk_wait'
                 env.PARENT_TASK = 'gatk_cc'
                 def ti =  env.BUILD_ID +'_gatk_wait'
                 env.ti = ti
                 sh "env >> env.txt"
                 //sh "python3 noop.py env.txt"
                 /
                 if (env.taskResultStageC == 'true') {
                    sh "python3 noop.py"
                    sh "echo ${env.taskIDStageC}"
                    sh "echo ${env.taskResultStageC}"  
                    env.taskIDStageD = 1
                    env.taskResultStageD = true
                    sh "echo ${env.taskIDStageD}"
                    sh "echo ${env.taskResultStageD}"
                 } else {
                    env.taskIDStageD = 0
                    env.taskResultStageD = false
                 }
                 //
              }
              //sh "echo ${env.taskIDStageD}"
              //sh "echo ${env.taskResultStageD}"
           }
        }
        stage('vcf_cc'){
            steps {
               script {
                  env.CURRENT_TASK = 'vcf_cc'
                  env.PARENT_TASK = 'gatk_wait'
                  def ti =  env.BUILD_ID +'_vcf_cc'
                  env.ti = ti
                  sh "env >> env.txt"
                  sh 'python3 create_cc.py env.txt'
                 //
                 if (env.taskResultStageC == 'true') {
                    sh "python3 create_cc.py"
                    sh "echo ${env.taskIDStageC}"
                    sh "echo ${env.taskResultStageC}"  
                    env.taskIDStageD = 1
                    env.taskResultStageD = true
                    sh "echo ${env.taskIDStageD}"
                    sh "echo ${env.taskResultStageD}"
                 } else {
                    env.taskIDStageD = 0
                    env.taskResultStageD = false
                 }
                 //
               }
               //sh "echo ${env.taskIDStageD}"
               //sh "echo ${env.taskResultStageD}"
            }    
        }
        stage('vcf_wait'){
            steps {
               script {
                 env.CURRENT_TASK = 'vcf_wait'
                 env.PARENT_TASK = 'vcf_cc'
                 def ti =  env.BUILD_ID +'_vcf_wait'
                 env.ti = ti
                 sh "env >> env.txt"
                 //sh "python3 noop.py env.txt"
                 //
                 if (env.taskResultStageC == 'true') {
                    sh 'python3 noop.py'
                    sh "echo ${env.taskIDStageC}"
                    sh "echo ${env.taskResultStageC}"  
                    env.taskIDStageD = 1
                    env.taskResultStageD = true
                    sh "echo ${env.taskIDStageD}"
                    sh "echo ${env.taskResultStageD}"
                 } else {
                    env.taskIDStageD = 0
                    env.taskResultStageD = false
                 }
                 //
               }
               //sh "echo ${env.taskIDStageD}"
               //sh "echo ${env.taskResultStageD}"
            }
          
        }
        */
    }
}
