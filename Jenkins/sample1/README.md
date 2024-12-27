# Make dir
```
mkdir -p ./jenkins_home
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

# How to use
```
http://localhost:8080/
```
Input Admin Password XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Dashboard -> Manage Jenkins -> Nodes -> New Nodes

* Node Name           : jenkins-agent1
* Number of executors : 1
* Remote FS root      : /home/jenkins
* Label               : agent

Dashboard -> Manage Jenkins -> Nodes -> agent1

copy the secret XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
and setting environment JENKINS_SECRET of jenkins-agent1 for docker-compose.yml

Restart docker
* stop : ctrl+c
* start: docker compose up

# down
```
docker compose down
```

