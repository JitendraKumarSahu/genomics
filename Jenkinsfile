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
                  params.each{param-> sh "echo ${param.key}=${param.value} >> env.txt"}
                  sh 'cat params.txt'
                  env.CURRENT_TASK = 'bwa_cc'
                  env.PARENT_TASK = null
                  def ti =  env.BUILD_ID +'_bwa_cc'
                  env.ti = ti
                  //sh 'echo "${BUILD_ID}_bwa_cc" >> env.ti'
                  sh "env >> env1.txt"
                  sh 'python3 create_cc.py params.txt env1.txt bwajob'
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
                  sh 'python3 create_cc.py env3.txt gatkjob'
               }
            }
        }
        stage('gatk_wait'){
            steps {
              script {
                 env.CURRENT_TASK = 'gatk_wait'
                 env.PARENT_TASK = 'gatk_cc'
                 def ti =  env.BUILD_ID +'_gatk_wait'
                 env.ti = ti
                 sh "env >> env4.txt"
                 sh "python3 noop.py env4.txt"
              }
           }
        }
        stage('vcf_cc'){
            steps {
               script {
                  env.CURRENT_TASK = 'vcf_cc'
                  env.PARENT_TASK = 'gatk_wait'
                  def ti =  env.BUILD_ID +'_vcf_cc'
                  env.ti = ti
                  sh "env >> env5.txt"
                  sh 'python3 create_cc.py env5.txt vcfjob'
               }
            }    
        }
        stage('vcf_wait'){
            steps {
               script {
                 env.CURRENT_TASK = 'vcf_wait'
                 env.PARENT_TASK = 'vcf_cc'
                 def ti =  env.BUILD_ID +'_vcf_wait'
                 env.ti = ti
                 sh "env >> env6.txt"
                 sh "python3 noop.py env6.txt"
               }
            }
        }
    }
}
