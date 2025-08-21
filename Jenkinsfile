pipeline {
    agent any

    environment {
        IMAGE_NAME = "ayushrockss/internship-project"
         
    }

    triggers {
        githubPush() // ✅ Fix the trigger: this is the correct name (case sensitive!)
    }

    stages {

        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-creds', branch: 'main', url: 'https://github.com/ayushrockss/Internship'
            }
        }




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
                    ssh -o StrictHostKeyChecking=no ubuntu@13.218.67.161 \"
                        sudo docker stop internship-container || true &&
                        sudo docker rm internship-container || true &&
                        sudo docker pull $IMAGE_NAME &&
                        # sudo docker run -d -p 80:5000 --name internship-container $IMAGE_NAME
                        sudo docker run -d \
                        --restart unless-stopped \
                        --network monitor-net \
                        -p 80:5000 \
                        --name internship-container \
                        $IMAGE_NAME
                    \"
                    """
                }
            }
        }
    }
}
