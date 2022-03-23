pipeline{
    agent any
    stages {
    stage ('addition')
        {
    steps {
          echo "hi this demo purpose only"
             }
          }
        stage ('email notification')
        {
            steps { emailext body: 'this is notification', subject: 'jenkins job', to: 'dnkumar@stratapps.com,vabhinav@stratapps.com'
                  }
            }
        }
    }
