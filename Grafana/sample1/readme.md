sudo service docker start
sudo chown 472:0 data/grafana
sudo docker-compose up -d

user : admin
pass : admin

# プラグインインストール
## Dockerファイルでインストール
environment:
    - GF_INSTALL_PLUGINS=marcusolsson-gantt-panel,grafana-googlesheets-datasource,grafana-mongodb-datasource

## コンテナに入ってインストール
grafana-cli plugins install grafana-mongodb-datasource