def setBuildStatus(String message, String state) {
        step([
            $class: "GitHubCommitStatusSetter",
            reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/my-org/my-repo"],
            contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
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
        }
        
        post {

            always {
                echo 'This will always run'  
            }

            success {
                
                echo 'This will run only if successful'
                steps{
                    setBuildStatus("Build complete", "SUCCESS")
                }
            } 

            failure {
            
                echo 'This will run only if fails'
                githubNotify status: 'FAILURE', account: 'dcarho', credentialsId: 'my-credentials',  repo: 'software-quality', context: 'Activity3 Test', description: 'This is an example'
                mail bcc: '', to: "dcarho@hotmail.com", body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}"
                         
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