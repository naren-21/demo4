pipeline{
    agent any
    stages {
       stage ('checkout'){
          steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/naren-21/demo4.git']]])
                }
        }
       stage ('programe1'){
          steps { 
                git branch: 'main', credentialsId: 'test123', url: 'https://github.com/naren-21/demo4.git'
                sh 'python3 task4.py'
                
                }
            }
        stage ('program2'){
          steps { 
                git branch: 'main', credentialsId: 'test123', url: 'https://github.com/naren-21/demo4.git'
                sh 'python3 greatsmall.py'
                 }
            }
        }
    }
