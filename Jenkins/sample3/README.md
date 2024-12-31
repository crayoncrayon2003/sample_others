# Make dir
```
./00_mkdir.sh
```
# Build and Run
```
docker compose up
```

# Setup
```
http://localhost:8080/
```
Input Admin Password XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Plugins
Manage Jenkins -> Manage Plugins -> Available Plugins
install follow
* Python
* Pyenv Pipeline Plugin

# Git integration
## preparation git repository
http://localhost/

* user: root
* pass: folloing
```
docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

Projects -> Create a project -> Create blank project
* Project name     : sample_project
* Project URL      : root
* Project slug     : sample_project
* Visibility Level : Private

```
git clone http://172.28.164.85/root/sample_project.git
```

the sample script push to Git.

```
./10_make_git_srcy.sh
cd sample_project
git add .
git commit -m "Add File"
git push origin main
```

## preparation access token
'avatar icon' in upper left -> Edit Profile -> 'access tokens' in the left menu -> Add new token
* Token name : MyToken
* Select scopes : Select 'read_repository'

copy personal access token.

## Create Pipeline
* name : case4

* General : GitHub project
    * Project url : http://172.28.164.85/root/sample_project.git

build parameter -> Authentication Parameters
    * name     : token
    * kind     : Secret text
defeult -> +add -> Jenkins
    * Domain   : global domain
    * kind     : Secret text
    * required : ON
    * scope    : global
    * secret   : paste gitlab repository access token
    * id       : id_accesstoken
* Build Trigger : Execute periodically
    * schedule : H/15 * * * *
* Build Environment : Do not select
* pipeline : pipeline script


```
pipeline {
    agent any

    environment {
        GIT_TOKEN = credentials('id_accesstoken')
        DIR_ROOT = "${env.WORKSPACE}"
        DIR_PROJ = "${DIR_ROOT}/sample_project"
        DIR_SRC  = "${DIR_PROJ}/src"
        DIR_TEST = "${DIR_PROJ}/test"
    }

    stages {
        stage('Stage0 Clean Existing Repository') {
            steps {
                sh '''
                if [ -d "${DIR_PROJ}" ]; then
                    rm -rf ${DIR_PROJ}
                fi
                '''
            }
        }
        stage('Stage1 Git Checkout') {
            steps {
                dir("${DIR_ROOT}") {
                    sh '''
                    git clone http://${GIT_TOKEN}:${GIT_TOKEN}@172.28.164.85/root/sample_project.git ${ROOT_DIR}
                    '''
                }
            }
        }
        stage('Stage1 Setup Virtual Environment') {
            steps {
                dir("${DIR_PROJ}") {
                    sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Stage3 Run Tests') {
            steps {
                dir("${DIR_PROJ}") {
                    sh '''
                    export PYTHONPATH=$PYTHONPATH:${DIR_PROJ}
                    . venv/bin/activate
                    pytest ${DIR_TEST}/test_main.py --html=report.html
                    '''
                }
            }
        }
        stage('Stage4 Clean Up') {
            steps {
                sh '''
                if [ -d "${DIR_PROJ}" ]; then
                    rm -rf ${DIR_PROJ}
                fi
                '''
            }
        }
    }
}

```