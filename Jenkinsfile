def setBuildStatus(String message, String state) {
        step([
            $class: "GitHubCommitStatusSetter",
            reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/dcarho/software-quality"],
            contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "Activity3-pipeline/build-status"],
            errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
            statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
        ]);
}
pipeline {
    agent any

    environment {
        
        GIT_COMMIT="${bat(returnStdout: true, script: 'git rev-parse HEAD')}"
    }   

    stages {

        stage('Preparation') {
            steps {
              echo 'Hello Preparation'
              bat 'C:/Users/prueba/AppData/Local/Programs/Python/Python313/python.exe -m pip install --upgrade pip'              
              bat 'if exist requirements.txt C:/Users/prueba/AppData/Local/Programs/Python/Python313/Scripts/pip.exe install -r requirements.txt'
            }
        }
        
        stage('Test') {

        steps {
            echo 'Hello Test'
            bat 'exit 1'
        }
        
        post {

            always {
                echo 'This will always run'  
            }

            success {
                
                echo 'This will run only if successful'
                setBuildStatus("Build complete", "SUCCESS")
                
            } 

            failure {
            
                echo 'This will run only if fails'
                setBuildStatus("Build complete", "FAILURE")
                mail bcc: '', to: "dcarho@hotmail.com", body: "<b>Los test fallaron.</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}",  charset: 'UTF-8', mimeType: 'text/html', subject: "ERROR CI: Project name -> ${env.JOB_NAME}"
                         
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