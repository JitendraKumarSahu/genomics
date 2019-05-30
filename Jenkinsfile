pipeline {
   environment {
       didSucceed = true
   }
   agent any
    stages {
         stage ('bwa_cc') {
            steps {
               script {
                  params.each{param-> sh "echo ${param.key}=${param.value} >> env_params.txt"}
                  sh 'cat env_params.txt'
                  env.CURRENT_TASK = 'bwa_cc'
                  env.PARENT_TASK = null
                  def ti =  env.BUILD_ID +'_bwa_cc'
                  env.ti = ti
                  sh "env >> env1.txt"
                  sh 'python3 create_cc.py env_params.txt env1.txt bwajob'
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
                  sh 'python3 create_cc.py env_params.txt env3.txt gatkjob'
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
                  sh 'python3 create_cc.py env_params.txt env5.txt vcfjob'
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
