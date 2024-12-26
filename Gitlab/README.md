# Make dir
```
./00_mkdir.sh
```

# Build and Run
```
docker run --rm -t -i -v $(pwd)/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register

docker compose up
```
wait for 5 minutes.

# How to use
Admin Username and Password
* Username: root
* Password: folling ...

```
docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
> Password: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

```
http://localhost/
```

Admin -> CI/CD -> Runners -> New instance runner -> Create Runner
* Tags                : example
* Runner description  : this is example
* Maximum job timeout : 600

Step1 -> Copy Token. Set tokens in /gitlab-runner/config.toml and Save.



# down
```
docker compose down
```

