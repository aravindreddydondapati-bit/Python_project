pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Syntax Validation') {
            steps {
                echo 'Validating main.py'
                sh 'python3 -m py_compile main.py'
            }
        }

        stage('Application Execution') {
            steps {
                echo 'Executing main.py'
                sh 'python3 main.py'
            }
        }
	stage('Syntax Validation') {
    	    steps {
        	echo 'Validating Python files'
       		 sh 'python3 -m py_compile main.py student.py'
    	    }
	}	
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL'
        }

        failure {
            echo 'BUILD FAILED'
        }

        always {
            echo 'Pipeline execution completed'
        }
    }
}
