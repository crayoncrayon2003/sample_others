
# make dir
```
mkdir -p ./data/mongo ./data/grafana
sudo chown 472:0 ./data/mongo ./data/grafana
```

# build and run
```
docker compose up -d
```

Access the following URL using the Web browser.
```
http://localhost:3000/
```
user : admin
pass : admin

# How to use
## Step1
Dashboards -> New -> New Dashboard -> Import a dashboard

select file : Step01_load_GrafanaDashboard.json

## Step2
```
sudo apt-get install python-dev default-libmysqlclient-dev
pip install mysqlclient
```

python Step02_input_mySqlData.py
