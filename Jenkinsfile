pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Sahithi08/jenkins_lab.git'
            }
        }
        stage('Build Code-1') {
            steps {
                sh "chmod u+x Prog1.py"
                sh "./Prog1.py"
            }
        }
	stage('Build Code-2') {
            steps {
                sh "chmod u+x Prog2.py"
                sh "./Prog2.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}

