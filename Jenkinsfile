```groovy
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
                echo 'Checking Python version'
                sh 'python3 --version'
            }
        }

        stage('Syntax Validation') {
            steps {
                echo 'Validating all Python files'

                sh '''
                    python3 -m py_compile student.py
                    python3 -m py_compile test_student.py
                    python3 -m py_compile marks.py
                    python3 -m py_compile test_marks.py
                '''

                echo 'Syntax validation successful'
            }
        }

        stage('Student Module Testing') {
            steps {
                echo 'Testing Student Management Module'
                sh 'python3 test_student.py'
            }
        }

        stage('Marks Module Testing') {
            steps {
                echo 'Testing Marks Management Module'
                sh 'python3 test_marks.py'
            }
        }
    }

    post {

        success {
            echo 'BUILD SUCCESSFUL'
            echo 'Student and Marks modules validated successfully'
        }

        failure {
            echo 'BUILD FAILED'
            echo 'Check Console Output for errors'
        }

        always {
            echo 'Pipeline execution completed'
        }
    }
}
```
