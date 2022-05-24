    pipeline {

        agent any
        stages {
            stage("Clear") {
                steps {
                    cleanWs()
                }
            }


            stage('Clone') {
                steps {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'FinalProject']],
                        userRemoteConfigs: [[
                            credentialsId: 'e440e931-9e60-4c40-b3d7-9fd12f63b978',
                            url: 'https://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@github.com/DoKep2/NEW.git']]
                    ])
                }
            }
            stage('Run docker-compose') {
                steps {
                    step([
                        $class: 'DockerComposeBuilder',
                        dockerComposeFile: 'finalProject/docker-compose.yml',
                        option: [$class: 'StartAllServices'],
                        useCustomDockerComposeFile: true
                    ])
                }
            }
        }

        post {
            always {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'alluredir']]
                ])
                cleanWs()
            }
        }
    }