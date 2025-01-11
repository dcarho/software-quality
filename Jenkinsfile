pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
              echo 'Hello Preparation'
              bat 'C:/Users/prueba/AppData/Local/Programs/Python/Python313/python.exe -m pip install --upgrade pip'
              bat 'dir'
              bat 'if ./requirements.txt exist C:/Users/prueba/AppData/Local/Programs/Python/Python313/Scripts/pip.exe install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Hello Test'
            }
        
        post {
         always {  
             echo 'This will always run'  
         }  
         success {
             githubNotify  status: 'SUCCESS', account: 'dcarho', credentialsId: 'a47911ea-107e-40a7-a6d3-e756b06fa557',  repo: 'software-quality', context: 'Activity3 Test', description: 'This is an example', echo 'This will run only if successful'
         }  
         failure {
            steps{
                githubNotify  status: 'SUCCESS', account: 'dcarho', credentialsId: 'a47911ea-107e-40a7-a6d3-e756b06fa557',  repo: 'software-quality', context: 'Activity3 Test', description: 'This is an example', echo 'This will run only if successful'
                mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "dcarho@hotmail.com";  
            }
             
         }  
         unstable {  
             echo 'This will run only if the run was marked as unstable'  
         }  
         changed {  
             echo 'This will run only if the state of the Pipeline has changed'  
             echo 'For example, if the Pipeline was previously failing but is now successful'  
         } 

    }
        }
        
    }    
}