pipeline {
   agent any

   stages {
      stage('Unit Test') {
         steps {
            sh "python3 -m  unittest discover -s tests"
         }
      }
      
      stage('Package') {
        steps {
           dir('dist') {
               deleteDir()
           }
           sh 'python3 setup.py sdist bdist_wheel'
           archiveArtifacts artifacts: 'dist/**', onlyIfSuccessful: true
        }
      }
      
      stage('Upload') {
          steps {
              withCredentials([[$class: 'UsernamePasswordMultiBinding', 
                credentialsId:'5956dcde-16bb-401a-a383-52f7fd3263e0', 
                usernameVariable: 'USERNAME', 
                passwordVariable: 'PASSWORD']]) {
                sh '''
                    python3 -m twine upload --repository-url http://devpi:8080/build/dev -u $USERNAME -p $PASSWORD dist/*
                '''
              }
          }
      }
   }
}
