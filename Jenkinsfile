pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
              echo 'Hello Preparation'
              bat 'C:/Users/prueba/AppData/Local/Programs/Python/Python313/python.exe -m pip install --upgrade pip'
              bat 'if [ -f requirements.txt ]; then C:/Users/prueba/AppData/Local/Programs/Python/Python313/Scripts/pip.exe install -r requirements.txt; fi'
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
             echo 'This will run only if successful'  
         }  
         failure {  
             mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "dcarho@hotmail.com";  
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