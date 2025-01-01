# Make dir
```
sudo chmod 777 *.sh
./00_mkdir.sh
```

# Build and Run
```
docker compose up
```

> jenkins | Jenkins initial setup is required. An admin user has been created and a password generated.
> jenkins | Please use the following password to proceed to installation:
> jenkins |
> jenkins | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
> jenkins |
> jenkins | This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX is Admin Password

# Setup
```
http://localhost:8080/
```
Input Admin Password XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Plugins
Manage Jenkins -> Manage Plugins -> Available Plugins
install follow
* HTTP Request
* Pipeline Utility Steps

# Create Job
https://www.jenkins.io/doc/pipeline/tour/getting-started/

## Case5
### Pipeline1
* name : case5

* General : Do not select
* Build Trigger : Execute periodically
    * schedule : H/15 * * * *
* Build Environment : Do not select
* pipeline : pipeline script

```
pipeline {
    agent any

    stages {
        stage('case5-1') {
            steps {
                script {
                    // build case5-1 with parameter
                    def job1Result = build job: 'data-api_get',
                        parameters: [
                            string(name: 'url', value: 'http://localhost:80'),
                            string(name: 'id', value: '1')
                        ],
                        propagate: false
                    def job1Output = job1Result.description
                    echo "Job 1 Result: ${job1Output}"
                }
            }
        }
        stage('case5-2') {
            steps {
                script {
                    // build case5-2 with parameter
                    def job2Result = build job: 'data-api_post',
                        parameters: [
                            string(name: 'url', value: 'http://localhost:80'),
                            string(name: 'id', value: '1'),
                            string(name: 'value', value: 'sample data')
                        ],
                        propagate: false
                    def job2Output = job2Result.description
                    echo "Job 2 Result: ${job2Output}"
                }
            }
        }
        stage('case5-3') {
            steps {
                script {
                    // build case5-3 with parameter
                    def job3Result = build job: 'data-api_get',
                        parameters: [
                            string(name: 'url', value: 'http://localhost:80'),
                            string(name: 'id', value: '1')
                        ],
                        propagate: false
                    def job3Output = job3Result.description
                    echo "Job 3 Result: ${job3Output}"


                }
            }
        }
    }

    post {
        always {
            script {
                echo "Pipeline completed."
            }
        }
    }
}
```

### Pipeline2
* name : data-api_get

* General : Do not select
* Build Trigger : Do not select
* Build Environment : Do not select
* pipeline : pipeline script

```
pipeline {
    agent any
    parameters {
        string(name: 'url', defaultValue: 'http://localhost:80', description: 'Parameter for Job1')
        string(name: 'id', defaultValue: '0', description: 'Parameter for Job1')
    }
    stages {
        stage('Job 1 Stage') {
            steps {
                script {
                    def response = httpRequest(
                        url: "${params.url}/data-api?id=${params.id}",
                        httpMode: 'GET',
                        contentType: 'APPLICATION_JSON'
                    )
                    currentBuild.description = response.content
                }
            }
        }
    }
    post {
        always {
            script {
                echo currentBuild.description
            }
        }
    }
}

```

### Pipeline3
* name : data-api_post

* General : Do not select
* Build Trigger : Do not select
* Build Environment : Do not select
* pipeline : pipeline script

```
pipeline {
    agent any
    parameters {
        string(name: 'url',   defaultValue: 'http://localhost:80', description: 'Parameter for Job1')
        string(name: 'id',    defaultValue: '0', description: 'Parameter for Job1')
        string(name: 'value', defaultValue: 'default value', description: 'Parameter for Job1')
    }
    stages {
        stage('Job 1 Stage') {
            steps {
                script {
                    def response = httpRequest(
                        url: "${params.url}/data-api",
                        httpMode: 'POST',
                        contentType: 'APPLICATION_JSON',
                        requestBody: '{"id": "${params.id}", "value": "${params.value}"}'
                    )
                    currentBuild.description = response.content
                }
            }
        }
    }
    post {
        always {
            script {
                echo currentBuild.description
            }
        }
    }
}

```


