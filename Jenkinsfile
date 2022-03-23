pipeline{
    agent any
    stages {
    stage ('addition')
        {
    steps {
    sh "./var/lib/jenkins/workspace/ppjob1/add.sh"
             }
          }
        stage ('email notification')
        {
            steps { emailext body: 'this is notification', subject: 'jenkins job', to: 'dnkumar@stratapps.com,vabhinav@stratapps.com'
                  }
            }
        }
    }
