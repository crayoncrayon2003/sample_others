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

Dashboard -> Manage Jenkins -> Nodes -> New Nodes
## jenkins-agent1
* Node Name           : jenkins-agent1
* Number of executors : 1
* Remote FS root      : /home/jenkins
* Label               : agent

## jenkins-agent2
* Node Name           : jenkins-agent2
* Number of executors : 1
* Remote FS root      : /home/jenkins
* Label               : agent

# Plugins
Manage Jenkins -> Manage Plugins -> Available Plugins
install follow
* Python
* Docker

# Create Job
https://www.jenkins.io/doc/pipeline/tour/getting-started/

* Freestyle Project
* Pipeline
* Multibranch Pipeline
* Folder
* Build Flow
* External Job
* Multi-configuration Project

## Case1
### Freestyle Project
* name : case1

* General : Do not select
* Source Code Management : Do not select
* Build Trigger : Execute periodically
    * schedule : H/15 * * * *
* Build Environment : Do not select
* Build Steps : Execute Shell
```
python3 -c 'print("Hello, Jenkins!")'
```

## Case2
### Freestyle Project
* name : case2

* General : Do not select
* Source Code Management : Do not select
* Build Trigger : Execute periodically
    * schedule : H/15 * * * *
* Build Environment : Do not select
* Build Steps : Execute Python script
```
# sample Python
print("Hello, Jenkins!")
```

## Case3
### Pipeline
* name : case3

* General : Do not select
* Build Trigger : Execute periodically
    * schedule : H/15 * * * *
* Build Environment : Do not select
* pipeline : pipeline script
```
pipeline {
    agent any
    stages {
        stage('Execute stage1') {
            steps {
                script {
                    // Assuming 'script1.py' is in the workspace
                    sh 'python script1.py'
                }
                script {
                    // Assuming 'script2.py' is in the workspace
                    sh 'python script2.py'
                }
            }
        }
        stage('Execute stage2') {
            steps {
                script {
                    // Assuming 'script3.py' is in the workspace
                    sh 'python script3.py'
                }
            }
        }
    }
}
```

create python file in "./workspace/case3"

