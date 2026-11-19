pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                echo 'Checking Python version'
                sh 'python3 --version'
            }
        }

        stage('Syntax Validation') {
            steps {
                echo 'Validating Python files'

                sh '''
                    python3 -m py_compile student.py
                    python3 -m py_compile test_student.py
                '''

                echo 'Python syntax validation successful'
            }
        }

        stage('Student Module Testing') {
            steps {
                echo 'Executing Student Management Tests'

                sh 'python3 test_student.py'
            }
        }
    }

    post {

        success {
            echo 'BUILD SUCCESSFUL'
            echo 'Student Management System validation completed successfully'
        }

        failure {
            echo 'BUILD FAILED'
            echo 'Please check the Jenkins Console Output for errors'
        }

        always {
            echo 'Pipeline execution completed'
        }
    }
}

