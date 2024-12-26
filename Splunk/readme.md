
# make dir
```
mkdir -p ./data/mysql ./data/splunk
sudo chown 472:0 ./data/mysql ./data/splunk
```

# build and run
```
docker compose up -d
```

Access the following URL using the Web browser.
```
http://localhost:8000
http://localhost:8000/ja-JP/
```
user : admin
pass : changeme

# How to use
* https://splunk.github.io/docker-splunk/EXAMPLES.html
* https://docs.splunk.com/Documentation
