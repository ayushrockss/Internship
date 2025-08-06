pipeline {
    agent any

    environment {
        IMAGE_NAME = "ayushrockss/internship-project"
       // SONAR_TOKEN = credentials('sonar-token') 
    }

    triggers {
        githubPush() // ✅ Fix the trigger: this is the correct name (case sensitive!)
    }

    stages {

        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-creds', branch: 'main', url: 'https://github.com/ayushrockss/flask-jenkins-docker-demo'
            }
        }
/*
        stage('Debug PATH') {
            steps {
                withEnv(["PATH+SONAR=/opt/sonar-scanner/bin"]) {
                    sh 'echo PATH=$PATH'
                    sh 'which sonar-scanner || echo "sonar-scanner not found!"'
                    sh 'sonar-scanner -v || echo "sonar-scanner not installed or not working"'
                }
            }
        }

        stage('Test Internet Access'){
            steps{
                sh 'curl -I https://sonarcloud.io || echo "❌ Cannot reach SonarCloud"'
            }
        }


        stage('SonarCloud Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    withEnv(["PATH+SONAR=/opt/sonar-scanner/bin"]) {
                        withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                            sh '''
                            echo "== ✅ SonarScanner Version Check =="
                            sonar-scanner -v

                            echo "== ✅ sonar-project.properties content =="
                            cat sonar-project.properties || echo "❌ File not found"

                            echo "== 🚀 Running Sonar Scanner with Debug =="
                            sonar-scanner -Dsonar.login=$SONAR_TOKEN -X
                            '''
                        }

                    }
                }
            }
        }

*/ 
// the above codes are first

//the below codes are second to be commneted dated 28-07-2025

/*
        stage('SonarCloud Code Analysis') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    sh '''
                    echo "👀 PATH Before:"
                    echo $PATH
                    export PATH=$PATH:/opt/sonar-scanner/bin
                    echo "🔍 sonar-scanner location:"
                    which sonar-scanner

                    sonar-scanner -X \
                    -Dsonar.projectKey=ayushrockss_flask-jenkins-docker-demo \
                    -Dsonar.organization=ayushrockss \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=https://sonarcloud.io \
                    -Dsonar.login=$SONAR_TOKEN \
                    -Dsonar.python.version=3.9
                    '''
                }
            }
        }
*/

/*
        stage('Install Python for Sonar') {
            steps {
                sh '''
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Debug PATH') {
            steps {
                withEnv(["PATH+SONAR=/opt/sonar-scanner/bin"]) {
                    sh 'echo PATH=$PATH'
                    sh 'which sonar-scanner || echo "sonar-scanner not found!"'
                    sh 'sonar-scanner -v || echo "sonar-scanner not installed or not working"'
                }
            }
        }


        stage('SonarCloud Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    withEnv(["PATH+SONAR=/opt/sonar-scanner/bin"]) {
                        sh 'sonar-scanner'
                    }
                }
            }
        }

*/

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login In Dockerhub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(credentials: ['ec2-ssh-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@44.211.124.230 \"
                        sudo docker stop internship-container || true &&
                        sudo docker rm internship-container || true &&
                        sudo docker pull $IMAGE_NAME &&
                        sudo docker run -d -p 80:5000 --name internship-container $IMAGE_NAME
                    \"
                    """
                }
            }
        }
    }
}
